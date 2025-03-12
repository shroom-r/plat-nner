document.querySelectorAll(".attendee-delete-form").forEach((form) =>
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    var form = event.currentTarget;
    var formData = new FormData(form);
    var url = form.action;
    fetch(url, {
      method: 'DELETE',
      body: formData,
    }).then((response) => {
      if (response.status == 200) {
        location.reload()
      }
      console.log(response);
    });
  })
);
