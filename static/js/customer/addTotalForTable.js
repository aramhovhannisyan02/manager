
// loop through all tables with id 'myTable'
document.querySelectorAll('table[id^="myTable"]').forEach(function(table) {
let total = 0;
// loop through all total_price cells in the current table and add their value to the total
table.querySelectorAll('#total_price').forEach(function(cell) {
    total += parseInt(cell.textContent);
});
// set the total value in the appropriate #totalPrice cell
table.querySelector('#totalPrice').textContent = total;
});

// Calculate and display the totals
var table = document.getElementById("debtTable");
var totalRow = table.rows[table.rows.length - 1];
var cellCount = totalRow.cells.length;
var columnSums = Array(cellCount).fill(0);

// Calculate the column sums
for (var i = 1; i < table.rows.length - 1; i++) {
    var row = table.rows[i];
    for (var j = 1; j < row.cells.length - 1; j++) {
        var cell = row.cells[j];
        var value = parseInt(cell.innerText.replace(' dram', ''));
        if (!isNaN(value)) {
            columnSums[j] += value;
        }
    }
};
totalRowCol = 0
// Display the column sums in the total row
for (var k = 1; k < totalRow.cells.length - 1; k++) {
    var totalCell = totalRow.cells[k];
    totalCell.innerText = columnSums[k] + " dram";
    totalRowCol += columnSums[k]
}

// Calculate the sum of the last row, including the last column
lastRowSum = 0;
lastRowCells = totalRow.cells.length - 1;
for (let l = 1; l < table.rows.length - 1; l++) {
    let row = table.rows[l];
    let lastCell = row.cells[lastRowCells];
    let value = parseInt(lastCell.innerText.replace(' dram', ''));
    if (!isNaN(value)) {
        lastRowSum += value;
    }
}

// Display the sum of the last column and the sum of the last row, including the last column, in the last cell of the Total row
// var lastTotalCell = totalRow.cells[totalRow.cells.length - 1];
// var lastColumnSum = parseInt(lastTotalCell.innerText.replace(' dram', ''));
// lastTotalCell.innerText = lastRowSum + "(" + (totalRowCol + lastRowSum) + " dram)";