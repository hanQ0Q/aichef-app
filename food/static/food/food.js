function updateItems() {
    var jsonDataElement = document.getElementById('dataVar');
    var jsonData = JSON.parse(jsonDataElement.textContent)
    var categoryDropdown = document.getElementById('categoryDropdown');
    var selectedCategory = categoryDropdown.value;

    // The items available for each category
    var itemsByCategory = jsonData

    var items = itemsByCategory[selectedCategory] || [];

    // Get the items dropdown and clear previous options
    var itemDropdown = document.getElementById('itemDropdown');
    itemDropdown.innerHTML = "";

    // Populate the items dropdown based on the selected category
    for (var i = 0; i < items.length; i++) {
        var option = document.createElement('option');
        option.value = items[i];
        option.textContent = items[i];
        itemDropdown.appendChild(option);
    }
}