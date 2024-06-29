#!/usr/bin/node
const fs = require('fs');
const path = require('path');

// Get command line arguments
const args = process.argv.slice(2); // Slice off 'node' and script name

// Ensure correct usage
if (args.length !== 3) {
  console.error('Usage: node 102-concat.js <fileA> <fileB> <fileC>');
  process.exit(1);
}

const fileAPath = args[0];
const fileBPath = args[1];
const fileCPath = args[2];

// Function to concatenate two files
function concatFiles(fileAPath, fileBPath, fileCPath) {
  // Read file A
  fs.readFile(fileAPath, 'utf8', (err, dataA) => {
    if (err) {
      console.error(`Error reading ${fileAPath}: ${err.message}`);
      process.exit(1);
    }

    // Read file B
    fs.readFile(fileBPath, 'utf8', (err, dataB) => {
      if (err) {
        console.error(`Error reading ${fileBPath}: ${err.message}`);
        process.exit(1);
      }

      // Concatenate data from both files
      const combinedData = dataA + '\n' + dataB + '\n'; // Add a newline between files

      // Write combined data to file C
      fs.writeFile(fileCPath, combinedData, 'utf8', (err) => {
        if (err) {
          console.error(`Error writing ${fileCPath}: ${err.message}`);
          process.exit(1);
        }
        console.log(`Files ${fileAPath} and ${fileBPath} have been concatenated to ${fileCPath}`);
      });
    });
  });
}

// Call function to concatenate files
concatFiles(fileAPath, fileBPath, fileCPath);
