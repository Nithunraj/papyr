const editBtn = document.getElementById("editProfileBtn");
const modal = document.getElementById("editProfileModal");

const passwordChangeBtn = document.getElementById("changePasswword");
const changePasswordModal = document.getElementById("changePasswordButton");

const closeButtons = document.querySelectorAll(".close-modal");
const modalOverlays = document.querySelectorAll(".modal-overlay");

editBtn.addEventListener("click", function (e) {
  e.preventDefault();
  modal.classList.add("active");
});

passwordChangeBtn.addEventListener("click", function (e) {
  e.preventDefault();
  changePasswordModal.classList.add("active");
});

closeButtons.forEach(btn => {
  btn.addEventListener("click", () => {
    modalOverlays.forEach(modal => modal.classList.remove("active"));
  });
});

// Close when clicking outside modal
modalOverlays.forEach(modal => {
  modal.addEventListener("click", e => {
    if (e.target === modal) {
      modal.classList.remove("active");
    }
  });
});