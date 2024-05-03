# EmailJS configuration

You have a *public key* here: <https://dashboard.emailjs.com/admin/account/general>

You have an *email service* that connects [EmailJS](https://emailjs.com) to your Fastmail account: <https://dashboard.emailjs.com/admin>

You have an *email template* here: <https://dashboard.emailjs.com/admin/templates/vb7khur/settings>

The include is [emailjs.html](_includes/emailjs.html). The Javascript refers to the public key, the email service, and the email template:

```javascript

emailjs.init({
    publicKey: "ktl5a0Y1Aqo03q9L7",
});

// lots of code ...


    // Send the form data using EmailJS
    emailjs.sendForm('service_re0ilxx', 'template_2xuxa5s', this)

```
