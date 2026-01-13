function handleSubmit() {
    var name1 = document.getElementById("person-name").value;
    var email1 = document.getElementById("person-email").value;
    var msg1 = document.getElementById("message-to-send").value;

    alert('Thank you for your message! I\'ll get back to you soon.');

    // If I ever do have a website, use this url (and set up the backend such that it makes a response)
    my_url = "kevinsony.xyz";
    fetch(my_url, {
        method: "POST",
        body: JSON.stringify({
            name: name1,
            email: email1,
            msg: msg1
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    });
}