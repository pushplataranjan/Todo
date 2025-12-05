# GitHub Issues for Todo Workshop App

This file contains 40 issues (20 Frontend + 20 Backend) ready to be created on GitHub for first-time contributors.

## How to Use This File

1. Copy each issue and create it on GitHub
2. Add appropriate labels: `good first issue`, `beginner-friendly`, `frontend` or `backend`
3. Assign difficulty level: `easy`, `medium`, or `hard`

---

## 🎨 FRONTEND ISSUES (20)

### Issue #1: Add Dark Mode Toggle
**Title:** Add Dark Mode Toggle to Todo App
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add a dark mode toggle button in the header that switches between light and dark themes. The theme preference should be saved in localStorage and persist across page reloads.

**Acceptance Criteria:**
- [ ] Dark mode toggle button in header
- [ ] Smooth transition between themes
- [ ] Theme preference saved in localStorage
- [ ] All UI elements properly styled for dark mode
- [ ] Toggle works on page reload

**Files to Modify:**
- `static/index.html`
- `static/styles.css`
- `static/app.js`

---

### Issue #2: Add Todo Priority Color Coding
**Title:** Add Visual Priority Indicators with Colors
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Enhance the todo cards to show priority with more prominent color coding. High priority should be red, medium orange, and low green.

**Acceptance Criteria:**
- [ ] Priority colors are clearly visible
- [ ] Color scheme is consistent
- [ ] Works with existing priority filter
- [ ] Accessible color contrast

**Files to Modify:**
- `static/styles.css`
- `static/app.js`

---

### Issue #3: Add Drag and Drop Reordering
**Title:** Implement Drag and Drop for Todo Reordering
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Allow users to reorder todos by dragging and dropping them. The order should be saved and persisted.

**Acceptance Criteria:**
- [ ] Todos can be dragged and dropped
- [ ] Visual feedback during drag
- [ ] Order persists after page reload
- [ ] Works on both desktop and touch devices

**Files to Modify:**
- `static/app.js`
- `static/styles.css`
- `backend/routes/todo_routes.py` (add order field)

---

### Issue #4: Add Todo Completion Animation
**Title:** Add Smooth Animation When Completing Todos
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add a smooth animation (fade out, checkmark animation) when a todo is marked as complete.

**Acceptance Criteria:**
- [ ] Smooth animation on completion
- [ ] Checkmark animation
- [ ] Visual feedback is clear
- [ ] Animation doesn't block UI

**Files to Modify:**
- `static/styles.css`
- `static/app.js`

---

### Issue #5: Add Todo Search Highlighting
**Title:** Highlight Search Terms in Todo Results
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
When searching, highlight the matching text in the todo title and description.

**Acceptance Criteria:**
- [ ] Search terms are highlighted
- [ ] Highlighting works in title and description
- [ ] Case-insensitive highlighting
- [ ] Multiple matches are highlighted

**Files to Modify:**
- `static/app.js`
- `static/styles.css`

---

### Issue #6: Add Todo Due Date Countdown
**Title:** Show Countdown Timer for Todos with Due Dates
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Display a countdown timer showing time remaining until the due date. Show "Overdue" in red for past due dates.

**Acceptance Criteria:**
- [ ] Countdown timer displayed
- [ ] Updates in real-time
- [ ] "Overdue" shown for past dates
- [ ] Clear visual indication

**Files to Modify:**
- `static/app.js`
- `static/styles.css`

---

### Issue #7: Add Todo Bulk Actions
**Title:** Implement Bulk Select and Actions for Todos
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add checkboxes to select multiple todos and perform bulk actions (delete, mark complete, change priority).

**Acceptance Criteria:**
- [ ] Checkboxes for selection
- [ ] Select all/none functionality
- [ ] Bulk delete, complete, priority change
- [ ] Visual feedback for selected items

**Files to Modify:**
- `static/index.html`
- `static/app.js`
- `static/styles.css`
- `backend/routes/todo_routes.py`

---

### Issue #8: Add Todo Categories Filter Dropdown
**Title:** Improve Category Filter with Dropdown
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Replace the category filter select with a better dropdown that shows all available categories with counts.

**Acceptance Criteria:**
- [ ] Dropdown shows all categories
- [ ] Shows count of todos per category
- [ ] Better visual design
- [ ] Easy to use

**Files to Modify:**
- `static/index.html`
- `static/app.js`
- `static/styles.css`

---

### Issue #9: Add Keyboard Shortcuts
**Title:** Implement Keyboard Shortcuts for Common Actions
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add keyboard shortcuts: `Ctrl+N` for new todo, `Ctrl+F` for search, `Esc` to close modals, etc.

**Acceptance Criteria:**
- [ ] Keyboard shortcuts documented
- [ ] Shortcuts work as expected
- [ ] Help modal showing shortcuts
- [ ] No conflicts with browser shortcuts

**Files to Modify:**
- `static/app.js`
- `static/index.html` (add help modal)

---

### Issue #10: Add Todo Export to CSV
**Title:** Add Export Todos to CSV Functionality
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add a button to export all todos (or filtered todos) to a CSV file that can be opened in Excel.

**Acceptance Criteria:**
- [ ] Export button in header
- [ ] Exports to CSV format
- [ ] Includes all todo fields
- [ ] Respects current filters
- [ ] File downloads automatically

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `static/styles.css`

---

### Issue #11: Add Todo Import from CSV
**Title:** Add Import Todos from CSV File
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Allow users to import todos from a CSV file. Show preview before importing.

**Acceptance Criteria:**
- [ ] Import button
- [ ] File picker for CSV
- [ ] Preview before import
- [ ] Error handling for invalid files
- [ ] Success/error feedback

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `backend/routes/todo_routes.py`

---

### Issue #12: Add Todo Templates
**Title:** Create Todo Templates for Common Tasks
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add predefined todo templates (e.g., "Meeting", "Project Task", "Personal") that users can quickly create.

**Acceptance Criteria:**
- [ ] Template selection in add form
- [ ] Pre-filled fields from template
- [ ] Multiple templates available
- [ ] Easy to use

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `static/styles.css`

---

### Issue #13: Add Todo Progress Bar
**Title:** Add Progress Bar Showing Completion Percentage
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add a progress bar in the stats section showing the percentage of completed todos.

**Acceptance Criteria:**
- [ ] Progress bar in stats section
- [ ] Shows completion percentage
- [ ] Updates in real-time
- [ ] Visual and accessible

**Files to Modify:**
- `static/index.html`
- `static/app.js`
- `static/styles.css`

---

### Issue #14: Add Todo Sorting Options
**Title:** Add Sort Options for Todo List
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add sorting options: by date, priority, title, or completion status.

**Acceptance Criteria:**
- [ ] Sort dropdown
- [ ] Multiple sort options
- [ ] Ascending/descending toggle
- [ ] Sort persists during session

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `static/styles.css`

---

### Issue #15: Add Todo Attachments/Images
**Title:** Add Image Upload for Todos
**Labels:** `frontend`, `enhancement`, `hard`
**Description:**
Allow users to attach images to todos. Display thumbnails in the todo card.

**Acceptance Criteria:**
- [ ] Image upload button
- [ ] Image preview
- [ ] Thumbnail display
- [ ] Image storage (backend needed)
- [ ] File size validation

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `backend/routes/todo_routes.py`
- `backend/models.py`

---

### Issue #16: Add Todo Comments Section
**Title:** Add Comments/Notes Section to Each Todo
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add a comments section to each todo where users can add multiple comments/notes.

**Acceptance Criteria:**
- [ ] Comments section in todo card
- [ ] Add/edit/delete comments
- [ ] Timestamp for each comment
- [ ] Expandable/collapsible

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `backend/models.py`
- `backend/routes/todo_routes.py`

---

### Issue #17: Add Todo Recurring Tasks
**Title:** Implement Recurring Todo Tasks
**Labels:** `frontend`, `enhancement`, `hard`
**Description:**
Allow users to create recurring todos (daily, weekly, monthly) that automatically create new instances.

**Acceptance Criteria:**
- [ ] Recurrence options in form
- [ ] Automatic creation of instances
- [ ] Recurrence pattern selection
- [ ] End date option

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `backend/models.py`
- `backend/routes/todo_routes.py`

---

### Issue #18: Add Todo Sharing Feature
**Title:** Add Share Todo via Link Functionality
**Labels:** `frontend`, `enhancement`, `medium`
**Description:**
Add a share button that generates a shareable link for a todo (read-only view).

**Acceptance Criteria:**
- [ ] Share button on todo card
- [ ] Generates shareable link
- [ ] Copy to clipboard
- [ ] Read-only view for shared link

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `backend/routes/todo_routes.py`

---

### Issue #19: Add Todo Calendar View
**Title:** Implement Calendar View for Todos
**Labels:** `frontend`, `enhancement`, `hard`
**Description:**
Add a calendar view showing todos organized by their due dates.

**Acceptance Criteria:**
- [ ] Calendar view toggle
- [ ] Todos displayed on calendar
- [ ] Click to view/edit todo
- [ ] Month navigation
- [ ] Responsive design

**Files to Modify:**
- `static/app.js`
- `static/index.html`
- `static/styles.css`

---

### Issue #20: Add Todo Print View
**Title:** Add Print-Friendly View for Todos
**Labels:** `frontend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add a print button that shows a clean, print-friendly view of all todos.

**Acceptance Criteria:**
- [ ] Print button
- [ ] Print-friendly layout
- [ ] Includes all todo information
- [ ] Proper page breaks
- [ ] Respects filters

**Files to Modify:**
- `static/styles.css`
- `static/app.js`
- `static/index.html`

---

## ⚙️ BACKEND ISSUES (20)

### Issue #21: Add Todo Validation
**Title:** Implement Input Validation for Todo Creation
**Labels:** `backend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add server-side validation for todo creation and updates. Validate title length, date formats, etc.

**Acceptance Criteria:**
- [ ] Title length validation (min 1, max 200)
- [ ] Date format validation
- [ ] Priority value validation
- [ ] Return clear error messages
- [ ] Tests for validation

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `backend/models.py`

---

### Issue #22: Add Pagination for Todos
**Title:** Implement Pagination for Todo List API
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add pagination to the GET /api/todos endpoint to handle large numbers of todos efficiently.

**Acceptance Criteria:**
- [ ] Pagination parameters (page, per_page)
- [ ] Returns pagination metadata
- [ ] Default page size
- [ ] Works with filters

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `static/app.js` (update frontend)

---

### Issue #23: Add Todo Search with Full-Text
**Title:** Implement Full-Text Search for Todos
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Improve search functionality with full-text search capabilities across title, description, and tags.

**Acceptance Criteria:**
- [ ] Full-text search implementation
- [ ] Searches title, description, tags
- [ ] Case-insensitive
- [ ] Returns relevant results
- [ ] Performance optimized

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `backend/models.py`

---

### Issue #24: Add Todo Archiving
**Title:** Implement Todo Archiving Feature
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add ability to archive completed todos instead of deleting them. Archived todos are hidden but can be restored.

**Acceptance Criteria:**
- [ ] Archive field in Todo model
- [ ] Archive endpoint
- [ ] Restore endpoint
- [ ] Filter archived todos
- [ ] Soft delete implementation

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `static/app.js`

---

### Issue #25: Add Todo Activity Log
**Title:** Create Activity Log for Todo Changes
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Track all changes to todos (created, updated, completed, deleted) with timestamps and user info.

**Acceptance Criteria:**
- [ ] Activity log model
- [ ] Log all todo changes
- [ ] GET endpoint for activity log
- [ ] Include user and timestamp
- [ ] Filterable by todo

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `backend/routes/activity_routes.py` (new file)

---

### Issue #26: Add Todo Reminders System
**Title:** Implement Scheduled Reminder System
**Labels:** `backend`, `enhancement`, `hard`
**Description:**
Create a background task system that sends reminders for todos based on due dates and user preferences.

**Acceptance Criteria:**
- [ ] Background task scheduler
- [ ] Reminder logic
- [ ] Configurable reminder times
- [ ] Email and browser notifications
- [ ] Prevents duplicate reminders

**Files to Modify:**
- `backend/services/notification_service.py`
- `backend/services/reminder_service.py` (new file)
- `app.py` (add scheduler)

---

### Issue #27: Add Todo Statistics API
**Title:** Enhance Statistics API with More Metrics
**Labels:** `backend`, `good first issue`, `enhancement`, `easy`
**Description:**
Expand the statistics endpoint to include more metrics: average completion time, most active category, etc.

**Acceptance Criteria:**
- [ ] Additional statistics calculated
- [ ] Average completion time
- [ ] Most used category
- [ ] Completion rate over time
- [ ] Performance optimized

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `static/app.js` (update frontend)

---

### Issue #28: Add Todo Duplicate Detection
**Title:** Implement Duplicate Todo Detection
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Detect and warn users when creating todos that are similar to existing ones (based on title similarity).

**Acceptance Criteria:**
- [ ] Similarity detection algorithm
- [ ] Warning on duplicate creation
- [ ] Configurable similarity threshold
- [ ] Returns similar todos
- [ ] Performance optimized

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `backend/services/todo_service.py` (new file)

---

### Issue #29: Add Todo Categories Management
**Title:** Create Categories CRUD API
**Labels:** `backend`, `good first issue`, `enhancement`, `easy`
**Description:**
Add endpoints to manage categories: create, list, update, delete categories.

**Acceptance Criteria:**
- [ ] Category model (if needed)
- [ ] CRUD endpoints
- [ ] Category validation
- [ ] Category usage count
- [ ] Prevent deletion if in use

**Files to Modify:**
- `backend/models.py`
- `backend/routes/category_routes.py` (new file)

---

### Issue #30: Add Todo Tags Management
**Title:** Implement Tags CRUD API
**Labels:** `backend`, `good first issue`, `enhancement`, `easy`
**Description:**
Create endpoints to manage tags separately, with autocomplete functionality.

**Acceptance Criteria:**
- [ ] Tag model
- [ ] CRUD endpoints
- [ ] Autocomplete endpoint
- [ ] Tag usage statistics
- [ ] Popular tags endpoint

**Files to Modify:**
- `backend/models.py`
- `backend/routes/tag_routes.py` (new file)

---

### Issue #31: Add Todo Export API
**Title:** Create API Endpoint for Todo Export
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add an API endpoint that exports todos in various formats (JSON, CSV, PDF).

**Acceptance Criteria:**
- [ ] Export endpoint
- [ ] Multiple format support
- [ ] Respects filters
- [ ] Proper file generation
- [ ] Error handling

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `backend/services/export_service.py` (new file)

---

### Issue #32: Add Todo Import API
**Title:** Create API Endpoint for Todo Import
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add an API endpoint to import todos from JSON or CSV files.

**Acceptance Criteria:**
- [ ] Import endpoint
- [ ] File upload handling
- [ ] Validation of imported data
- [ ] Batch creation
- [ ] Error reporting

**Files to Modify:**
- `backend/routes/todo_routes.py`
- `backend/services/import_service.py` (new file)

---

### Issue #33: Add Todo Collaboration
**Title:** Implement Multi-User Todo Sharing
**Labels:** `backend`, `enhancement`, `hard`
**Description:**
Allow multiple users to collaborate on todos. Add sharing permissions and user assignments.

**Acceptance Criteria:**
- [ ] User assignment to todos
- [ ] Sharing permissions
- [ ] Collaboration endpoints
- [ ] Notification on assignment
- [ ] Access control

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `backend/services/collaboration_service.py` (new file)

---

### Issue #34: Add Todo Version History
**Title:** Implement Version History for Todos
**Labels:** `backend`, `enhancement`, `hard`
**Description:**
Track version history of todos, allowing users to see changes and revert to previous versions.

**Acceptance Criteria:**
- [ ] Version history model
- [ ] Track all changes
- [ ] Revert functionality
- [ ] Version comparison
- [ ] History endpoint

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `backend/services/version_service.py` (new file)

---

### Issue #35: Add Todo Attachments API
**Title:** Implement File Attachment System for Todos
**Labels:** `backend`, `enhancement`, `hard`
**Description:**
Add ability to attach files to todos. Handle file uploads, storage, and retrieval.

**Acceptance Criteria:**
- [ ] File upload endpoint
- [ ] File storage system
- [ ] File retrieval endpoint
- [ ] File size limits
- [ ] File type validation
- [ ] Secure file handling

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `backend/services/file_service.py` (new file)

---

### Issue #36: Add Todo Comments API
**Title:** Create Comments System for Todos
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Implement a comments system where users can add comments to todos.

**Acceptance Criteria:**
- [ ] Comment model
- [ ] CRUD endpoints for comments
- [ ] Comments linked to todos
- [ ] User attribution
- [ ] Timestamps

**Files to Modify:**
- `backend/models.py`
- `backend/routes/comment_routes.py` (new file)

---

### Issue #37: Add Todo Recurrence API
**Title:** Implement Recurring Todos API
**Labels:** `backend`, `enhancement`, `hard`
**Description:**
Add support for recurring todos with various recurrence patterns (daily, weekly, monthly).

**Acceptance Criteria:**
- [ ] Recurrence model
- [ ] Recurrence pattern parsing
- [ ] Automatic instance creation
- [ ] Recurrence endpoints
- [ ] End date handling

**Files to Modify:**
- `backend/models.py`
- `backend/routes/todo_routes.py`
- `backend/services/recurrence_service.py` (new file)

---

### Issue #38: Add Todo Analytics API
**Title:** Create Analytics Endpoint for Todo Usage
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Create an analytics endpoint that provides insights: completion trends, productivity metrics, etc.

**Acceptance Criteria:**
- [ ] Analytics calculation
- [ ] Completion trends
- [ ] Productivity metrics
- [ ] Time-based analytics
- [ ] Performance optimized

**Files to Modify:**
- `backend/routes/analytics_routes.py` (new file)
- `backend/services/analytics_service.py` (new file)

---

### Issue #39: Add Todo API Rate Limiting
**Title:** Implement Rate Limiting for API Endpoints
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add rate limiting to prevent API abuse. Use Flask-Limiter or similar.

**Acceptance Criteria:**
- [ ] Rate limiting middleware
- [ ] Configurable limits
- [ ] Per-endpoint limits
- [ ] Clear error messages
- [ ] Documentation

**Files to Modify:**
- `app.py`
- `requirements.txt`
- `backend/routes/*.py`

---

### Issue #40: Add Todo API Caching
**Title:** Implement Caching for Todo API Responses
**Labels:** `backend`, `enhancement`, `medium`
**Description:**
Add caching to improve API performance, especially for frequently accessed endpoints like stats and lists.

**Acceptance Criteria:**
- [ ] Caching implementation
- [ ] Cache invalidation
- [ ] Configurable TTL
- [ ] Performance improvement
- [ ] Cache statistics

**Files to Modify:**
- `app.py`
- `backend/routes/todo_routes.py`
- `requirements.txt`

---

## 📝 Notes

- All issues should be created with appropriate labels
- Add difficulty estimates based on contributor experience
- Consider breaking down larger issues into smaller tasks
- Update this file as issues are created and resolved
- Link related issues together

