// Main JavaScript file for Pine Labs Integration Assistant

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Auto-hide alerts after 5 seconds
    setTimeout(function() {
        var alerts = document.querySelectorAll('.alert');
        alerts.forEach(function(alert) {
            var bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        });
    }, 5000);
});

// Utility functions
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function() {
        showToast('Copied to clipboard!', 'success');
    }, function(err) {
        console.error('Could not copy text: ', err);
        showToast('Failed to copy to clipboard', 'error');
    });
}

function showToast(message, type = 'info') {
    // Create toast element
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.setAttribute('role', 'alert');
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">${message}</div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>
    `;
    
    // Add to toast container
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
        toastContainer.style.zIndex = '9999';
        document.body.appendChild(toastContainer);
    }
    
    toastContainer.appendChild(toast);
    
    // Show toast
    const bsToast = new bootstrap.Toast(toast);
    bsToast.show();
    
    // Remove from DOM after hiding
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}

// Form validation helpers
function validateRequired(fieldId, fieldName) {
    const field = document.getElementById(fieldId);
    if (!field.value.trim()) {
        field.classList.add('is-invalid');
        showToast(`${fieldName} is required`, 'danger');
        return false;
    }
    field.classList.remove('is-invalid');
    return true;
}

function validateEmail(fieldId) {
    const field = document.getElementById(fieldId);
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (field.value && !emailRegex.test(field.value)) {
        field.classList.add('is-invalid');
        showToast('Please enter a valid email address', 'danger');
        return false;
    }
    field.classList.remove('is-invalid');
    return true;
}

function validateAmount(fieldId) {
    const field = document.getElementById(fieldId);
    const amount = parseFloat(field.value);
    
    if (field.value && (isNaN(amount) || amount <= 0)) {
        field.classList.add('is-invalid');
        showToast('Please enter a valid amount greater than 0', 'danger');
        return false;
    }
    field.classList.remove('is-invalid');
    return true;
}

// API helper functions
function makeAPIRequest(endpoint, method = 'GET', data = null) {
    const config = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    if (data) {
        config.body = JSON.stringify(data);
    }
    
    return fetch(endpoint, config)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .catch(error => {
            console.error('API request failed:', error);
            showToast('API request failed. Please try again.', 'danger');
            throw error;
        });
}

// Loading state management
function setLoading(element, loading = true) {
    if (loading) {
        element.disabled = true;
        element.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...';
    } else {
        element.disabled = false;
        element.innerHTML = element.getAttribute('data-original-text') || 'Submit';
    }
}

// Save original button text
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('button').forEach(button => {
        button.setAttribute('data-original-text', button.innerHTML);
    });
});