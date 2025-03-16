/**
 * Add event listener to showAddPostForm button
 * On click, show form
 */

import { initializeElementsVisibility } from "./initializeElementsVisibility.js";

document.querySelectorAll(".showNewPostFormButton").forEach((el) =>
  el.addEventListener("click", (event) => {
    initializeElementsVisibility()
    var target = event.currentTarget;
    var parent = target.closest(".event-card");
    // Show wanted form, hide button and set focus on first input
    var form = parent.querySelector(".newPostFormContainer");
    form.classList.remove("hidden");
    form.scrollIntoView({ behavior: "smooth"});
    parent.querySelector(".showNewPostFormButton").classList.add("hidden");
    form.querySelector("input#name").focus()
  })
);
