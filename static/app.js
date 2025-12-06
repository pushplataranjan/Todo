// API Base URL
const API_BASE = '/api';

// Global State
let currentUser = null;
let todos = [];
let notifications = [];
let filters = {
    completed: null,
    priority: '',
    category: '',
    search: ''
};

// Initialize App
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
    setupEventListeners();
    requestNotificationPermission();
    loadInitialData();
    startNotificationPolling();
});

// Initialize App
function initializeApp() {
    // Create default user if none exists
    createDefaultUser();
}

// Setup Event Listeners
function setupEventListeners() {
    // Add Todo
    document.getElementById('addTodoBtn').addEventListener('click', toggleTodoForm);
    document.getElementById('cancelBtn').addEventListener('click', toggleTodoForm);
    document.getElementById('todoForm').addEventListener('submit', handleCreateTodo);

    // Filters
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.addEventListener('click', (e) => handleFilterClick(e.target));
    });
    document.getElementById('searchInput').addEventListener('input', handleSearch);
    document.getElementById('priorityFilter').addEventListener('change', handlePriorityFilter);
    document.getElementById('categoryFilter').addEventListener('change', handleCategoryFilter);

    // Modals
    document.getElementById('notificationBtn').addEventListener('click', openNotificationModal);
    document.getElementById('settingsBtn').addEventListener('click', openSettingsModal);
    
    const printBtn = document.getElementById('printBtn');
    if (printBtn) printBtn.addEventListener('click', handlePrint);
    document.getElementById('closeNotificationModal').addEventListener('click', closeNotificationModal);
    document.getElementById('closeSettingsModal').addEventListener('click', closeSettingsModal);

    // Settings
    document.getElementById('saveUserBtn').addEventListener('click', saveUserSettings);
    document.getElementById('emailNotifications').addEventListener('change', updateNotificationSettings);
    document.getElementById('browserNotifications').addEventListener('change', updateNotificationSettings);

    // Close modals on outside click
    document.getElementById('notificationModal').addEventListener('click', (e) => {
        if (e.target.id === 'notificationModal') closeNotificationModal();
    });
    document.getElementById('settingsModal').addEventListener('click', (e) => {
        if (e.target.id === 'settingsModal') closeSettingsModal();
    });
}

// API Functions
async function apiCall(endpoint, method = 'GET', data = null) {
    const options = {
        method,
        headers: {
            'Content-Type': 'application/json'
        }
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(`${API_BASE}${endpoint}`, options);
        const result = await response.json();
        
        if (!response.ok) {
            throw new Error(result.error || 'API request failed');
        }
        
        return result;
    } catch (error) {
        console.error('API Error:', error);
        showToast(error.message, 'error');
        throw error;
    }
}

// User Management
async function createDefaultUser() {
    try {
        const users = await apiCall('/users');
        if (users.length === 0) {
            currentUser = await apiCall('/users', 'POST', {
                username: 'workshop_user',
                email: 'workshop@example.com',
                email_notifications_enabled: true,
                browser_notifications_enabled: true
            });
        } else {
            currentUser = users[0];
        }
        loadUserSettings();
    } catch (error) {
        console.error('Error creating user:', error);
    }
}

async function loadUserSettings() {
    if (!currentUser) return;
    
    document.getElementById('userName').value = currentUser.username || '';
    document.getElementById('userEmail').value = currentUser.email || '';
    document.getElementById('emailNotifications').checked = currentUser.email_notifications_enabled;
    document.getElementById('browserNotifications').checked = currentUser.browser_notifications_enabled;
}

async function saveUserSettings() {
    if (!currentUser) return;
    
    try {
        const username = document.getElementById('userName').value;
        const email = document.getElementById('userEmail').value;
        
        currentUser = await apiCall(`/users/${currentUser.id}`, 'PUT', {
            username,
            email,
            email_notifications_enabled: document.getElementById('emailNotifications').checked,
            browser_notifications_enabled: document.getElementById('browserNotifications').checked
        });
        
        showToast('Settings saved successfully!', 'success');
        closeSettingsModal();
    } catch (error) {
        showToast('Failed to save settings', 'error');
    }
}

async function updateNotificationSettings() {
    if (!currentUser) return;
    
    try {
        currentUser = await apiCall(`/users/${currentUser.id}`, 'PUT', {
            email_notifications_enabled: document.getElementById('emailNotifications').checked,
            browser_notifications_enabled: document.getElementById('browserNotifications').checked
        });
    } catch (error) {
        console.error('Error updating notification settings:', error);
    }
}

// Todo Functions
async function loadTodos() {
    try {
        let endpoint = '/todos';
        const params = new URLSearchParams();
        
        if (filters.completed !== null) {
            params.append('completed', filters.completed);
        }
        if (filters.priority) {
            params.append('priority', filters.priority);
        }
        if (filters.category) {
            params.append('category', filters.category);
        }
        if (filters.search) {
            params.append('search', filters.search);
        }
        if (currentUser) {
            params.append('user_id', currentUser.id);
        }
        
        if (params.toString()) {
            endpoint += '?' + params.toString();
        }
        
        todos = await apiCall(endpoint);
        renderTodos();
        updateStats();
        updateCategories();
    } catch (error) {
        document.getElementById('todosContainer').innerHTML = '<div class="empty-state"><h3>Error loading todos</h3></div>';
    }
}

function renderTodos() {
    const container = document.getElementById('todosContainer');
    
    if (todos.length === 0) {
        container.innerHTML = '<div class="empty-state"><h3>No todos found</h3><p>Create your first todo to get started!</p></div>';
        return;
    }
    
    container.innerHTML = todos.map(todo => createTodoCard(todo)).join('');
    
    // Add event listeners to todo cards
    todos.forEach(todo => {
        document.getElementById(`complete-${todo.id}`)?.addEventListener('click', () => toggleComplete(todo.id));
        document.getElementById(`delete-${todo.id}`)?.addEventListener('click', () => deleteTodo(todo.id));
        document.getElementById(`edit-${todo.id}`)?.addEventListener('click', () => editTodo(todo));
    });
}

function createTodoCard(todo) {
    const dueDate = todo.due_date ? new Date(todo.due_date).toLocaleDateString() : 'No due date';
    const tags = todo.tags && todo.tags.length > 0 
        ? todo.tags.map(tag => `<span class="tag">${tag}</span>`).join('')
        : '';
    
    return `
        <div class="todo-card ${todo.completed ? 'completed' : ''} ${todo.priority}-priority" id="todo-${todo.id}">
            <div class="todo-header">
                <h3 class="todo-title">${escapeHtml(todo.title)}</h3>
                <div class="todo-actions">
                    <button class="btn-small btn-complete" id="complete-${todo.id}">
                        ${todo.completed ? '↩️ Undo' : '✓ Complete'}
                    </button>
                    <button class="btn-small btn-edit" id="edit-${todo.id}">✏️ Edit</button>
                    <button class="btn-small btn-delete" id="delete-${todo.id}">🗑️ Delete</button>
                </div>
            </div>
            ${todo.description ? `<p class="todo-description">${escapeHtml(todo.description)}</p>` : ''}
            <div class="todo-meta">
                <span>📅 ${dueDate}</span>
                <span>🏷️ ${todo.priority}</span>
                ${todo.category ? `<span>📁 ${escapeHtml(todo.category)}</span>` : ''}
            </div>
            ${tags ? `<div class="todo-tags">${tags}</div>` : ''}
        </div>
    `;
}

async function handleCreateTodo(e) {
    e.preventDefault();
    
    const title = document.getElementById('todoTitle').value;
    const description = document.getElementById('todoDescription').value;
    const priority = document.getElementById('todoPriority').value;
    const dueDate = document.getElementById('todoDueDate').value;
    const category = document.getElementById('todoCategory').value;
    const tagsInput = document.getElementById('todoTags').value;
    const tags = tagsInput ? tagsInput.split(',').map(t => t.trim()).filter(t => t) : [];
    
    try {
        const todoData = {
            title,
            description,
            priority,
            category: category || null,
            tags,
            user_id: currentUser?.id || null
        };
        
        if (dueDate) {
            todoData.due_date = new Date(dueDate).toISOString();
        }
        
        await apiCall('/todos', 'POST', todoData);
        showToast('Todo created successfully!', 'success');
        document.getElementById('todoForm').reset();
        toggleTodoForm();
        loadTodos();
        loadNotifications();
    } catch (error) {
        showToast('Failed to create todo', 'error');
    }
}

async function toggleComplete(todoId) {
    try {
        await apiCall(`/todos/${todoId}/complete`, 'POST');
        showToast('Todo updated!', 'success');
        loadTodos();
        loadNotifications();
    } catch (error) {
        showToast('Failed to update todo', 'error');
    }
}

async function deleteTodo(todoId) {
    if (!confirm('Are you sure you want to delete this todo?')) return;
    
    try {
        await apiCall(`/todos/${todoId}`, 'DELETE');
        showToast('Todo deleted!', 'success');
        loadTodos();
        loadNotifications();
    } catch (error) {
        showToast('Failed to delete todo', 'error');
    }
}

function editTodo(todo) {
    document.getElementById('todoTitle').value = todo.title;
    document.getElementById('todoDescription').value = todo.description || '';
    document.getElementById('todoPriority').value = todo.priority;
    document.getElementById('todoDueDate').value = todo.due_date ? todo.due_date.split('T')[0] : '';
    document.getElementById('todoCategory').value = todo.category || '';
    document.getElementById('todoTags').value = todo.tags ? todo.tags.join(', ') : '';
    
    if (document.getElementById('todoForm').classList.contains('hidden')) {
        toggleTodoForm();
    }
    
    // Change form to update mode
    const form = document.getElementById('todoForm');
    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.textContent = 'Update Todo';
    submitBtn.onclick = async (e) => {
        e.preventDefault();
        await updateTodo(todo.id);
    };
}

async function updateTodo(todoId) {
    const title = document.getElementById('todoTitle').value;
    const description = document.getElementById('todoDescription').value;
    const priority = document.getElementById('todoPriority').value;
    const dueDate = document.getElementById('todoDueDate').value;
    const category = document.getElementById('todoCategory').value;
    const tagsInput = document.getElementById('todoTags').value;
    const tags = tagsInput ? tagsInput.split(',').map(t => t.trim()).filter(t => t) : [];
    
    try {
        const todoData = {
            title,
            description,
            priority,
            category: category || null,
            tags
        };
        
        if (dueDate) {
            todoData.due_date = new Date(dueDate).toISOString();
        }
        
        await apiCall(`/todos/${todoId}`, 'PUT', todoData);
        showToast('Todo updated successfully!', 'success');
        document.getElementById('todoForm').reset();
        toggleTodoForm();
        loadTodos();
        loadNotifications();
        
        // Reset form button
        const submitBtn = document.getElementById('todoForm').querySelector('button[type="submit"]');
        submitBtn.textContent = 'Create Todo';
        submitBtn.onclick = null;
    } catch (error) {
        showToast('Failed to update todo', 'error');
    }
}

// Filter Functions
function handleFilterClick(btn) {
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    
    const filter = btn.dataset.filter;
    if (filter === 'all') {
        filters.completed = null;
    } else if (filter === 'completed') {
        filters.completed = 'true';
    } else if (filter === 'pending') {
        filters.completed = 'false';
    } else if (filter === 'high') {
        filters.priority = 'high';
    }
    
    loadTodos();
}

function handleSearch(e) {
    filters.search = e.target.value;
    loadTodos();
}

function handlePriorityFilter(e) {
    filters.priority = e.target.value;
    loadTodos();
}

function handleCategoryFilter(e) {
    filters.category = e.target.value;
    loadTodos();
}

function updateCategories() {
    const categories = [...new Set(todos.map(t => t.category).filter(c => c))];
    const select = document.getElementById('categoryFilter');
    const currentValue = select.value;
    
    select.innerHTML = '<option value="">All Categories</option>' + 
        categories.map(cat => `<option value="${cat}">${cat}</option>`).join('');
    select.value = currentValue;
}

// Stats Functions
async function updateStats() {
    try {
        const endpoint = currentUser ? `/todos/stats?user_id=${currentUser.id}` : '/todos/stats';
        const stats = await apiCall(endpoint);
        
        document.getElementById('totalTodos').textContent = stats.total;
        document.getElementById('completedTodos').textContent = stats.completed;
        document.getElementById('pendingTodos').textContent = stats.pending;
        document.getElementById('highPriorityTodos').textContent = stats.high_priority;
    } catch (error) {
        console.error('Error loading stats:', error);
    }
}

// Notification Functions
function requestNotificationPermission() {
    if ('Notification' in window && Notification.permission === 'default') {
        Notification.requestPermission();
    }
}

async function loadNotifications() {
    if (!currentUser) return;
    
    try {
        notifications = await apiCall(`/notifications?user_id=${currentUser.id}&pending_only=true`);
        updateNotificationBadge();
    } catch (error) {
        console.error('Error loading notifications:', error);
    }
}

function updateNotificationBadge() {
    const count = notifications.filter(n => !n.sent).length;
    document.getElementById('notificationCount').textContent = count;
    document.getElementById('notificationCount').style.display = count > 0 ? 'flex' : 'none';
}

function openNotificationModal() {
    document.getElementById('notificationModal').classList.remove('hidden');
    renderNotifications();
}

function closeNotificationModal() {
    document.getElementById('notificationModal').classList.add('hidden');
}

function renderNotifications() {
    const container = document.getElementById('notificationsList');
    
    if (notifications.length === 0) {
        container.innerHTML = '<p>No notifications</p>';
        return;
    }
    
    container.innerHTML = notifications.map(notif => `
        <div class="notification-item ${notif.sent ? '' : 'unread'}" onclick="markNotificationRead(${notif.id})">
            <strong>${escapeHtml(notif.message)}</strong>
            <div style="font-size: 0.8rem; color: #6b7280; margin-top: 5px;">
                ${new Date(notif.created_at).toLocaleString()}
            </div>
        </div>
    `).join('');
}

async function markNotificationRead(notificationId) {
    try {
        await apiCall(`/notifications/${notificationId}/mark-read`, 'POST');
        loadNotifications();
        renderNotifications();
    } catch (error) {
        console.error('Error marking notification as read:', error);
    }
}

function showBrowserNotification(title, body) {
    if ('Notification' in window && Notification.permission === 'granted' && currentUser?.browser_notifications_enabled) {
        new Notification(title, {
            body,
            icon: '/static/favicon.ico'
        });
    }
}

function startNotificationPolling() {
    setInterval(() => {
        loadNotifications();
    }, 30000); // Poll every 30 seconds
}

// Settings Modal
function openSettingsModal() {
    document.getElementById('settingsModal').classList.remove('hidden');
    loadUserSettings();
}

function closeSettingsModal() {
    document.getElementById('settingsModal').classList.add('hidden');
}

// UI Helpers
function toggleTodoForm() {
    document.getElementById('todoForm').classList.toggle('hidden');
    if (!document.getElementById('todoForm').classList.contains('hidden')) {
        document.getElementById('todoTitle').focus();
    }
}

function showToast(message, type = 'success') {
    const container = document.getElementById('toastContainer');
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    container.appendChild(toast);
    
    setTimeout(() => {
        toast.remove();
    }, 3000);
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Print functions
function buildFiltersSummary() {
        const parts = [];
        if (filters.completed === 'true') parts.push('Completed');
        else if (filters.completed === 'false') parts.push('Pending');
        if (filters.priority) parts.push(`Priority: ${filters.priority}`);
        if (filters.category) parts.push(`Category: ${filters.category}`);
        if (filters.search) parts.push(`Search: "${filters.search}"`);
        return parts.length ? parts.join(' · ') : 'All todos';
}

function handlePrint() {
        try {
                // Use the currently-loaded todos (they reflect applied filters)
                const items = todos.slice();

                const printWindow = window.open('', '_blank');
                if (!printWindow) {
                        showToast('Unable to open print window (blocked by browser?)', 'error');
                        return;
                }

                const header = document.querySelector('.header h1')?.textContent || 'Todos';
                const filtersSummary = buildFiltersSummary();

                const content = `<!doctype html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width,initial-scale=1">
    <title>${escapeHtml(header)} - Print</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        body { background: #fff; color: #111; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif; padding: 18px; }
        .print-header { margin-bottom: 18px; }
        .print-header h2 { margin: 0 0 6px 0; font-size: 1.2rem; }
        .print-filters { color: #444; margin-bottom: 6px; }
        .todo-card { box-shadow: none; border-radius: 6px; margin-bottom: 12px; padding: 12px; }
        .todo-meta { color: #444; font-size: 0.95rem; }
        .todo-tags .tag { background: #111; color: #fff; }
        @media print { .page-break { page-break-after: always; } }
    </style>
</head>
<body>
    <div class="print-header">
        <div>
            <h2>${escapeHtml(header)}</h2>
            <div class="print-filters">${escapeHtml(filtersSummary)}</div>
        </div>
        <div style="text-align:right; color:#666; font-size:0.9rem">Printed: ${new Date().toLocaleString()}</div>
    </div>
    <main>
        ${items.length === 0 ? '<p>No todos to print</p>' : items.map(todo => {
                const dueDate = todo.due_date ? new Date(todo.due_date).toLocaleDateString() : 'No due date';
                const tags = todo.tags && todo.tags.length ? todo.tags.map(t => `<span class="tag">${escapeHtml(t)}</span>`).join('') : '';
                const completed = todo.completed ? '<strong>(Completed)</strong>' : '';
                return `
                    <article class="todo-card ${todo.priority}-priority">
                        <div style="display:flex;justify-content:space-between;align-items:flex-start;">
                            <div style="flex:1">
                                <div class="todo-title">${escapeHtml(todo.title)} ${completed}</div>
                                ${todo.description ? `<div class="todo-description" style="margin-top:6px">${escapeHtml(todo.description)}</div>` : ''}
                            </div>
                        </div>
                        <div class="todo-meta" style="margin-top:8px">
                            <span>📅 ${escapeHtml(dueDate)}</span>
                            <span style="margin-left:12px">🏷️ ${escapeHtml(todo.priority)}</span>
                            ${todo.category ? `<span style="margin-left:12px">📁 ${escapeHtml(todo.category)}</span>` : ''}
                        </div>
                        ${tags ? `<div class="todo-tags" style="margin-top:8px">${tags}</div>` : ''}
                    </article>
                `;
        }).join('')}
    </main>
</body>
</html>`;

                printWindow.document.open();
                printWindow.document.write(content);
                printWindow.document.close();

                // Give browser a moment to render styles before printing
                setTimeout(() => {
                        try {
                                printWindow.focus();
                                printWindow.print();
                        } catch (err) {
                                console.error('Print error:', err);
                        }
                }, 500);
        } catch (err) {
                console.error('handlePrint error:', err);
                showToast('An error occurred preparing print view', 'error');
        }
}

// Load Initial Data
async function loadInitialData() {
    await loadTodos();
    await loadNotifications();
}

