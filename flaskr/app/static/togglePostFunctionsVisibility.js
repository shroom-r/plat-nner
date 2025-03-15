/**
 * Add click listeners on attendee name to show toggle action buttons visibility
 */

document.querySelectorAll(".toggle-post-functions-button").forEach((el) => {
  el.addEventListener("click", (event) => {
    var target = event.currentTarget.closest(".post-container");
    // parent = target.closest(".post-container");
    var targetIsSelected = target.classList.contains("selected");
    // Unselect all selected names
    document
      .querySelectorAll(".post-container")
      .forEach((el) => el.classList.remove("selected"));
    document
      .querySelectorAll(".post-functions-container")
      .forEach((el) => el.classList.add("hidden"));
    if (!targetIsSelected) {
      target.classList.add("selected");
      target
        .querySelector(".post-functions-container")
        .classList.remove("hidden");
    }
  });
});
