// static/stripe.js
console.log("Sanity check!");

// Get Stripe publishable key
fetch("/config")
.then((result) => { 
  console.log("result back")
  return result.json(); 
}).then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe(data.publicKey);
  console.log("stripe initialized")

  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    const id = document.querySelector("#submitBtn").value;
    console.log("clicked")
    console.log(id)
    
    // Get Checkout Session ID
    fetch("/create-checkout-session/" + id)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });

  document.querySelector("#submitBtn").addEventListener("touchstart", () => {
    const id = document.querySelector("#submitBtn").value;
    console.log("touchstart")
    console.log(id)
    
    // Get Checkout Session ID
    fetch("/create-checkout-session/" + id)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});