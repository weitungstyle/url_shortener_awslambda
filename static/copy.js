async function copyUrl () {
  // Get the text field
  var copyText = document.getElementById("shortenUrl").textContent

  // Copy the text inside the text field
  await navigator.clipboard.writeText(copyText)

  // Alert the copied text
  alert("Copied the text: " + copyText)
}
