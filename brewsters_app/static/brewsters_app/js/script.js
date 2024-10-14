//js code for collapsible menu
const toggleBtn = document.getElementById('toggle-btn');
const sidebar = document.getElementById('sidebar');
const content = document.getElementById('content');

toggleBtn.addEventListener('click', () => {
    if (window.innerWidth <= 800) {
        sidebar.classList.toggle('active');
        content.classList.toggle('active');
    } else {
        sidebar.classList.toggle('collapsed');
        content.classList.toggle('collapsed');
    }
});

window.addEventListener('resize', () => {
    if (window.innerWidth <= 800) {
        sidebar.classList.add('collapsed');
        content.classList.add('collapsed');
        sidebar.classList.remove('active');
        content.classList.remove('active');
    } else {
        sidebar.classList.remove('collapsed');
        content.classList.remove('collapsed');
    }
});

// Check screen size on page load
if (window.innerWidth <= 800) {
    sidebar.classList.add('collapsed');
    content.classList.add('collapsed');
    sidebar.classList.remove('active');
    content.classList.remove('active');
} else {
    sidebar.classList.remove('collapsed');
    content.classList.remove('collapsed');
}

/*
<ul>
                {% for category in categories %}
                <li>
                    <h3>{{ category.categoryName }}</h3>
                    <p>{{ category.categoryImage }}</p>
                </li>
                {% empty %}
                <li>No items found.</li>
                {% endfor %}
            </ul>
*/