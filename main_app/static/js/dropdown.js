document.addEventListener('click', evt => {
  const isDropdownButton = evt.target.matches("[data-dropdown-button]")
  if (!isDropdownButton && evt.target.closest("[data-dropdown]") != null) return

  let dropdown
  if (isDropdownButton) {
    dropdown = evt.target.closest("[data-dropdown]")
    dropdown.classList.toggle("active")
  }

  let currentDropdown = document.querySelector("[data-dropdown].active")
  let button = document.querySelector("[data-dropdown-button]")
  if (currentDropdown && evt.target === button) {
    button.classList.toggle('btn-active')
    if (button.classList.contains('btn-inactive')) {
      button.classList.remove('btn-inactive')
    }
  } else if (!currentDropdown && evt.target === button) {
    button.classList.toggle('btn-inactive')
    button.classList.remove('btn-active')
  }
})