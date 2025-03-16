/**
 * Defin function to initialize all elements
 * On escape key press, initialize all elements visibility
 */

document.addEventListener("keydown", (event) => {
  if (event.key == "Escape") {
    initializeElementsVisibility();
  }
});

export function initializeElementsVisibility() {
  // Show all add attendee buttons
  document
    .querySelectorAll(".toggle-add-attendee-form-button")
    .forEach((el) => el.classList.remove("hidden"));
  // Hide all add attendee forms
  document
    .querySelectorAll(".addAttendeeFormContainer")
    .forEach((el) => el.classList.add("hidden"));

  // Hide all new post forms and show all new post buttons
  document
    .querySelectorAll(".newPostFormContainer")
    .forEach((el) => el.classList.add("hidden"));
  document
    .querySelectorAll(".showNewPostFormButton")
    .forEach((el) => el.classList.remove("hidden"));

  // Unselect all selected attendees and hide all function buttons
  document
    .querySelectorAll(".attendee-name")
    .forEach((el) => el.classList.remove("selected"));
  document
    .querySelectorAll(".attendee-functions-container")
    .forEach((el) => el.classList.add("hidden"));

  // Unselect all posts and hide all function buttons
  document
    .querySelectorAll(".post-container")
    .forEach((el) => el.classList.remove("selected"));
  document
    .querySelectorAll(".post-functions-container")
    .forEach((el) => el.classList.add("hidden"));

  // Hide new event form
  document.querySelector("#new-event-card").classList.add("hidden");

  // Unselect all event cards and hide all function buttons
  document
    .querySelectorAll(".event-card")
    .forEach((el) => el.classList.remove("selected"));
  document
    .querySelectorAll(".event-functions-container")
    .forEach((el) => el.classList.add("hidden"));
}
