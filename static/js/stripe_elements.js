var stripe = Stripe('pk_test_51HBhUUFztXrGefLPWk7yydAue6hohVGEd5NmUauyjdwg6o0VCJ6CAxM6JgkEjpBH70tdUXoPqX7BEpnbKRp7gLPW00PjlKlTlF');
var elements = stripe.elements();

var style = {
  base: {
    color: "#32325d",
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: "antialiased",
    fontSize: "16px",
    "::placeholder": {
      color: "#aab7c4"
    }
  },
  invalid: {
    color: "#fa755a",
    iconColor: "#fa755a"
  }
};

var cardElement = elements.create("card", { style: style });
cardElement.mount("#card-element");

var form = document.getElementById('subscription-form');