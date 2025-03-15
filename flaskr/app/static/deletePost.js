/**
 * Add submit event listener to delete post form.
 * Fetch API with DELETE method on submit, to delete post
 */
document.querySelectorAll(".post-delete-form").forEach((form) =>
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
