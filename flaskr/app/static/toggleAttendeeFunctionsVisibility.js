/**
 * Add click listeners on attendee name to show toggle action buttons visibility
 */

document.querySelectorAll(".attendee-name").forEach((el) => {
  el.addEventListener("click", (event) => {
    target = event.currentTarget;
    targetIsSelected = target.classList.contains("selected");
    // Unselect all selected names
    document
      .querySelectorAll(".attendee-name")
      .forEach((el) => el.classList.remove("selected"));
    document
      .querySelectorAll(".attendee-functions-container")
      .forEach((el) => el.classList.add("hidden"));
    if (!targetIsSelected) {
      target.classList.add("selected");
      target.parentNode.querySelector(".attendee-functions-container").classList.remove("hidden")
    }
  });
});
