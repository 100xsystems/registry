#!/usr/bin/env node
/**
 * restructure-languages.mjs
 *
 * Converts flat JSON files in static-data/knowledge/languages/
 *   javascript.json
 *   python.json
 *   all-resources.json
 *   index.json
 *
 * Into per-language folder structure:
 *   javascript/index.json
 *   python/index.json
 */

import * as fs from 'node:fs';
import * as path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const LANG_DIR = path.resolve(__dirname, '..', 'static-data', 'knowledge', 'languages');

// Get all JSON files (excluding all-resources.json and index.json)
const files = fs.readdirSync(LANG_DIR)
  .filter(f => f.endsWith('.json'))
  .filter(f => f !== 'all-resources.json' && f !== 'index.json');

let converted = 0;

for (const file of files) {
  const slug = file.replace(/\.json$/, '');
  const folderPath = path.join(LANG_DIR, slug);
  const indexPath = path.join(folderPath, 'index.json');

  // Create folder
  fs.mkdirSync(folderPath, { recursive: true });

  // Read source JSON and write as index.json inside folder
  const data = JSON.parse(fs.readFileSync(path.join(LANG_DIR, file), 'utf-8'));
  fs.writeFileSync(indexPath, JSON.stringify(data, null, 2) + '\n', 'utf-8');

  // Delete the flat file
  fs.unlinkSync(path.join(LANG_DIR, file));

  converted++;
}

// Delete all-resources.json and index.json
for (const f of ['all-resources.json', 'index.json']) {
  const fp = path.join(LANG_DIR, f);
  if (fs.existsSync(fp)) {
    fs.unlinkSync(fp);
    console.log(`  Deleted ${f}`);
  }
}

console.log(`\n✅ Converted ${converted} languages into folder structure`);
console.log(`📁 ${LANG_DIR}/`);
