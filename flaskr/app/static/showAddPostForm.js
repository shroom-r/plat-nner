/**
 * Add event listener to showAddPostForm button
 * On click, show form
 */
document.querySelectorAll(".showNewPostFormButton").forEach((el) =>
  el.addEventListener("click", (event) => {
    var target = event.currentTarget;
    var parent = target.closest(".event-card");
    // Hide all forms and show all buttons
    document
      .querySelectorAll(".newPostFormContainer")
      .forEach((el) => el.classList.add("hidden"));
    document
      .querySelectorAll(".showNewPostFormButton")
      .forEach((el) => el.classList.remove("hidden"));
    // Show wanted form and hide button
    parent.querySelector(".newPostFormContainer").classList.remove("hidden");
    parent.querySelector(".showNewPostFormButton").classList.add("hidden");
  })
);
