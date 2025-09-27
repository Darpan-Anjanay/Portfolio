function loadProfile(profileName) {
  fetch(`/profile/${profileName}/`)
    .then((response) => {
      if (!response.ok) {
        const container = document.querySelector(".container");
        if (container) container.style.display = "none";

        const message = `
  <div class="container mt-5">
    <div class="card text-white bg-danger">
      <div class="card-body">
        <p class="card-text mb-0">Profile not found.</p>
      </div>
    </div>
  </div>`;

        document.body.innerHTML += message;
      }
      return response.json();
    })
    .then((data) => {
      if (data) {
        const img = document.getElementById("profileImage");
        if (img) img.src = data.profile_image;

        const full_name = document.getElementById("full_name");
        if (full_name) full_name.textContent = data.full_name;

        const working_as = document.getElementById("working_as");
        if (working_as) working_as.textContent = data.working_as;

        const bio = document.getElementById("bio");
        if (bio) bio.innerHTML = data.bio;

        const resume = document.getElementById("resume-link");
        if (resume) resume.href = data.resume;

        const contact_number = document.getElementById("contact_number");
        if (contact_number) contact_number.textContent = data.contact_number;

        const email = document.getElementById("email");
        if (email) email.textContent = data.email;

        let socialLinksHTML = "";

        if (data.social_links && data.social_links.length > 0) {
          data.social_links.forEach((link) => {
            socialLinksHTML += `
            <a href="${link.link}" class="btn btn-primary btn-sm me-2" target="_blank">
              ${link.platform_name}
            </a>`;
          });
        }

        const links = document.getElementById("social-links");
        if (links) links.innerHTML = socialLinksHTML;

        const skills_Overview = document.getElementById("skills_Overview");
        if (skills_Overview) skills_Overview.innerHTML = data.skills_Overview;

        const Technology = document.getElementById("Technology");
        let TechnologyHTML = "";
        const techcategory = data.techcategory_set;

        if (techcategory && techcategory.length > 0) {
          const fetchTechPromises = techcategory.map((tech) => {
            return fetch(`/technology/${profileName}/${tech.id}/`)
              .then((response) => response.json())
              .then((techdata) => {
                let techshmtl = "";
                techdata.forEach((te) => {
                  techshmtl += `<li>${te.name}</li>`;
                });

                return `
                <div class="col mb-3">
                    <div class="technology card-theme">
                    <div class="techcategory">${tech.name}</div>
                    <ul>${techshmtl}</ul>
                    </div>
                </div>
                `;
              });
          });

          Promise.all(fetchTechPromises)
            .then((results) => {
              TechnologyHTML = results.join("");
              if (Technology) {
                Technology.innerHTML = TechnologyHTML;
              }
            })
            .catch((error) => console.error("Tech Fetch Error:", error));
        }
      }
    })
    .catch((error) => console.error("Error:", error));

  fetch(`/workhistory/${profileName}/`)
    .then((response) => response.json())
    .then((workdata) => {
      if (workdata) {
        const Workhistroy = document.getElementById("Workhistroy");
        let Workhistroyhtml = "";
        workdata.forEach((work) => {
          Workhistroyhtml += `
             <div class="col-lg-12 col-md-12 mb-3">
                <div class="card-theme">
                    <h5>${work.designation} | ${work.company_name}</h5>
                  <small>
  ${new Date(work.start_date).toLocaleString("default", {
    month: "short",
    year: "numeric",
  })} - ${
            work.present
              ? "Present"
              : new Date(work.end_date).toLocaleString("default", {
                  month: "short",
                  year: "numeric",
                })
          }
</small>

                    <p>${work.description}</p>
                </div>
            </div>
            `;
        });
        if (Workhistroy) {
          Workhistroy.innerHTML = Workhistroyhtml;
        }
      }
    })
    .catch((error) => console.error("Error:", error));

  fetch(`/project/${profileName}/`)
    .then((response) => response.json())
    .then((projectdata) => {
      if (projectdata) {
        const project = document.getElementById("Projects");
        let projecthtml = "";
        projectdata.forEach((project) => {
          let usedtech = "";
          project.techs.forEach((pr, index) => {
            usedtech += pr.name;
            if (index !== project.techs.length - 1) {
              usedtech += ",";
            }
          });

          projecthtml += `
            <div class="col-lg-12 col-md-12 mb-3">
  <div class="card-theme">
    <div class="card-body">
      <h5>${project.name}</h5>
      <p>${project.description}</p>

      <p class="mb-2">
        Tech Stack:
        ${usedtech}
      </p>

      <div class="text-end">
        <a href="${project.github_link}" class="btn btn-primary btn-sm" target="_blank">
          <i class="bi bi-github me-1"></i> View on GitHub
        </a>
      </div>
    </div>
  </div>
</div>

            `;
        });
        if (project) {
          project.innerHTML = projecthtml;
        }
      }
    })
    .catch((error) => console.error("Error:", error));
}

function getParamFromQuery() {
  const urlParams = new URLSearchParams(window.location.search);
  return urlParams.get("p");
}

window.onload = function () {
  const param = getParamFromQuery();
  if (param) loadProfile(param);
};

const themeToggleBtn = document.getElementById("themeToggle");

function setTheme(theme) {
  document.documentElement.setAttribute("data-theme", theme);
  localStorage.setItem("theme", theme);

  const icon = theme === "dark" ? "bi-sun-fill" : "bi-moon-fill";
  themeToggleBtn.innerHTML = `<i class="bi ${icon}"></i>`;
}

const savedTheme = localStorage.getItem("theme") || "dark";
setTheme(savedTheme);

themeToggleBtn.addEventListener("click", () => {
  const current = document.documentElement.getAttribute("data-theme");
  const next = current === "light" ? "dark" : "light";
  setTheme(next);
});
