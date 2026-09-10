const currentYear =
    document.querySelector("#current-year");


if (currentYear) {

    currentYear.textContent =
        new Date().getFullYear();

}


/* =========================
   MOBILE MENU
========================= */

const menuToggle =
    document.querySelector("#menu-toggle");

const nav =
    document.querySelector("#nav");


if (menuToggle && nav) {

    menuToggle.addEventListener(
        "click",
        () => {

            nav.classList.toggle(
                "nav--open"
            );


            const isOpen =
                nav.classList.contains(
                    "nav--open"
                );


            menuToggle.setAttribute(
                "aria-expanded",
                isOpen
            );


            menuToggle.textContent =
                isOpen
                    ? "×"
                    : "☰";

        }
    );


    nav
        .querySelectorAll("a")
        .forEach((link) => {

            link.addEventListener(
                "click",
                () => {

                    nav.classList.remove(
                        "nav--open"
                    );


                    menuToggle.setAttribute(
                        "aria-expanded",
                        "false"
                    );


                    menuToggle.textContent =
                        "☰";

                }
            );

        });

}


/* =========================
   FAQ
========================= */

const faqQuestions =
    document.querySelectorAll(
        ".faq-question"
    );


faqQuestions.forEach(
    (question) => {

        question.addEventListener(
            "click",
            () => {

                const currentItem =
                    question.closest(
                        ".faq-item"
                    );


                const alreadyOpen =
                    currentItem.classList.contains(
                        "faq-item--open"
                    );


                document
                    .querySelectorAll(
                        ".faq-item"
                    )
                    .forEach((item) => {

                        item.classList.remove(
                            "faq-item--open"
                        );


                        const button =
                            item.querySelector(
                                ".faq-question"
                            );


                        const icon =
                            item.querySelector(
                                ".faq-icon"
                            );


                        if (button) {

                            button.setAttribute(
                                "aria-expanded",
                                "false"
                            );

                        }


                        if (icon) {

                            icon.textContent =
                                "+";

                        }

                    });


                if (!alreadyOpen) {

                    currentItem.classList.add(
                        "faq-item--open"
                    );


                    question.setAttribute(
                        "aria-expanded",
                        "true"
                    );


                    const icon =
                        question.querySelector(
                            ".faq-icon"
                        );


                    if (icon) {

                        icon.textContent =
                            "−";

                    }

                }

            }
        );

    }
);


/* =========================
   FORMSPREE FORM
========================= */

const contactForm =
    document.querySelector(
        "#contact-form"
    );


const submitButton =
    document.querySelector(
        "#submit-button"
    );


const formStatus =
    document.querySelector(
        "#form-status"
    );


if (
    contactForm &&
    submitButton &&
    formStatus
) {

    contactForm.addEventListener(
        "submit",
        async (event) => {

            event.preventDefault();


            if (
                !contactForm.checkValidity()
            ) {

                contactForm.reportValidity();

                return;

            }


            submitButton.disabled = true;

            submitButton.textContent =
                "Sending...";


            formStatus.textContent =
                "";


            const formData =
                new FormData(
                    contactForm
                );


            try {

                const response =
                    await fetch(
                        contactForm.action,
                        {
                            method: "POST",

                            body: formData,

                            headers: {
                                Accept:
                                    "application/json"
                            }
                        }
                    );


                if (response.ok) {

                    formStatus.textContent =
                        "Thanks! Your request has been sent successfully.";


                    contactForm.reset();

                } else {

                    const data =
                        await response.json();


                    if (
                        data.errors &&
                        data.errors.length > 0
                    ) {

                        formStatus.textContent =
                            data.errors
                                .map(
                                    (error) =>
                                        error.message
                                )
                                .join(" ");

                    } else {

                        formStatus.textContent =
                            "Something went wrong. Please try again.";

                    }

                }

            } catch (error) {

                formStatus.textContent =
                    "Unable to send your request right now. Please try again.";

                console.error(
                    "Form submission error:",
                    error
                );

            } finally {

                submitButton.disabled =
                    false;


                submitButton.textContent =
                    "Request a Quote";

            }

        }
    );

}