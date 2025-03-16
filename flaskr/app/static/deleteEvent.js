/**
 * Add submit event listener to delete event form.
 * Fetch API with DELETE method on submit, to delete event
 */
document.querySelectorAll(".event-delete-form").forEach((form) =>
  form.addEventListener("submit", (event) => {
    event.preventDefault();
    var form = event.currentTarget;
    var formData = new FormData(form);
    var url = form.action;
    fetch(url, {
      method: "DELETE",
      body: formData,
    }).then((response) => {
        location.reload();
    });
  })
);
