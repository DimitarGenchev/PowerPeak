baseUrl = 'https://powerpeak-fudzdsacbqanbwd7.italynorth-01.azurewebsites.net';
const language = document.documentElement.lang;

if (language === 'en') {
    baseUrl += '/en';
}

document.addEventListener('DOMContentLoaded', async function () {
    await fetchAndFilterProducts();
});

const searchForm = document.querySelector('.search-form')

searchForm.addEventListener('submit', async function (e) {
    e.preventDefault();

    await fetchAndFilterProducts();
});

async function fetchAndFilterProducts() {
    const search = document.getElementById('search-input').value;
    const category = document.getElementById('product-category-input').value;
    const brand = document.getElementById('product-brand-input').value;

    const queryParams = new URLSearchParams({search, category, brand}).toString();

    try {
        const response = await fetch(`${baseUrl}/api/products/?${queryParams}`);
        const data = await response.json();

        const productsContainer = document.querySelector('.products-container');
        const productCount = document.querySelector('.products-count span');

        productsContainer.innerHTML = '';

        productCount.textContent = data.count;

        data.products.forEach(productHTML => {
            productsContainer.insertAdjacentHTML('beforeend', productHTML);
        });
    } catch (error) {
        console.error('Error fetching products:', error);
    }
}
