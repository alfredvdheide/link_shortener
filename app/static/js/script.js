console.log("I am a script!")


document.getElementById('submit-input').addEventListener('click', function () {
	let longUrl = document.getElementById('long-url').value;
	let shortUrl = document.getElementById('short-url').value;
	let isEvil = document.getElementById('is-evil').checked;
	
	fetch(`/submit_url`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({
			'longUrl': longUrl,
			'shortUrl': shortUrl,
			'isEvil': isEvil
		})
	})
			.then(response => response.json().then(data => ({data: data, response: response})))
			.then(res => {
				const data = res.data;
				const response = res.response;
				
				if (data.message) {
					// Show the server response message as a toast.
					Swal.fire({
						toast: true,
						position: 'bottom-end',
						showConfirmButton: false,
						timer: 3000,
						icon: 'success',
						title: data.message,
					});
				}
				
				if (!response.ok) {
					// If the request failed, log the status text to the console.
					console.error('Error:', response.statusText);
					Swal.fire({
						toast: true,
						position: 'bottom-end',
						showConfirmButton: false,
						timer: 3000,
						icon: 'danger',
						title: data.message,
					});
				}
			})
			.catch((error) => {
				// If the fetch failed, log the error to the console.
				console.error('Error:', error);
			});
});


/*datatables*/
$(document).ready(function () {
	$('#urlTable').DataTable({
		responsive: true,
		order: [[4, 'desc']],
		ajax: '/urls',
		columns: [
			{data: 'id'},
			{data: 'longUrl'},
			{data: 'shortUrl'},
			{data: 'isEvil'},
			{data: 'timestamp_utc'},
		]
	});
});
