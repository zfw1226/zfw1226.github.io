// Exercise the actual Liquid inline script without making network requests.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '../..');
let script = fs.readFileSync(path.join(root, '_includes/fetch_google_scholar_stats.html'), 'utf8');
script = script.replace(/<\/?script>/g, '');
script = script.replace(/{% if site.google_scholar_stats_use_cdn %}([\s\S]*?){% else %}[\s\S]*?{% endif %}/, '$1');
script = script.replace(/{{ site.repository }}/g, 'zfw1226/zfw1226.github.io');

function exercise(data, total, papers) {
  const document = {
    getElementById: () => total,
    getElementsByClassName: () => papers
  };
  const $ = () => ({ ready: callback => callback() });
  $.getJSON = (url, callback) => {
    assert.match(url, /gs_data\.json\?ts=\d+$/);
    callback(data);
    return { fail() {} };
  };
  vm.runInNewContext(script, { $, document, console });
}
function paper(id) {
  return { textContent: '', innerHTML: '', getAttribute: () => id };
}

const total = { textContent: '', innerHTML: '', hidden: true, title: '' };
exercise({ citedby: 2754, updated: '2026-10-11 23:41:54', publications: {} }, total, []);
assert.equal(total.textContent, '(2,754 citations)');
assert.equal(total.hidden, false);
assert.match(total.title, /2026-10-11/);

const known = paper('known');
const missing = paper('missing');
exercise({ citedby: 2754, publications: { known: { num_citations: 12 } } }, null, [missing, known]);
assert.equal(known.textContent, '| Citations: 12');
assert.equal(missing.textContent, '');

const invalid = { textContent: '', hidden: true };
exercise({ citedby: null }, invalid, []);
assert.equal(invalid.textContent, '');
assert.equal(invalid.hidden, true);
exercise(null, null, []);

const zero = { textContent: '', hidden: true };
exercise({ citedby: 0, publications: {} }, zero, []);
assert.equal(zero.textContent, '(0 citations)');
assert.equal(zero.hidden, false);

const profile = fs.readFileSync(path.join(root, '_includes/author-profile.html'), 'utf8');
assert.equal((profile.match(/id=["']total_cit["']/g) || []).length, 1);
assert.match(profile, /Google Scholar[\s\S]*?id=["']total_cit["']/);
assert.ok(!fs.readFileSync(path.join(root, '_pages/about.md'), 'utf8').includes('id="total_cit"'));
console.log('Frontend checks passed: sidebar placement, formatted count, missing DOM/paper, invalid data, zero count.');
