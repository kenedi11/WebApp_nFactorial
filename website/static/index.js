document.querySelector('#save-event-btn').addEventListener('click', function() {
    var event_id = document.querySelector('#event-id').value;
    
    fetch('/save_event', {
        method: 'POST',
        body: new URLSearchParams({
            'event_id': event_id
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
    })
    .then(response => {
        if (response.ok) {
            // Handle success
            console.log('Event saved successfully!');
        } else {
            // Handle failure
            console.error('Failed to save event');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
