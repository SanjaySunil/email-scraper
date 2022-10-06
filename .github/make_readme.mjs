import README from "readme-components";
let template = new README({});

template.metadata = {
  name: "email-scraper",
  description: "Generate thousands of temporary emails within seconds!",
  report_bug:
    "https://github.com/SanjaySunil/email-scraper/issues/new?assignees=&labels=Bug&template=bug_report.md&title=%5BBUG%5D",
  request_feature:
    "https://github.com/SanjaySunil/email-scraper/issues/new?assignees=&labels=Suggestions&template=suggestions.md&title=%5BSUGGESTION%5D",
  author: {
    name: "Sanjay Sunil",
    email: "sanjaysunil@protonmail.com",
  },
  license: "MIT",
};

template.use_premade("header", {
  name: template.metadata.name,
  description: template.metadata.description,
  report_bug: template.metadata.report_bug,
  request_feature: template.metadata.request_feature,
});

template.use_component("./readme_components/preview.md", {preview_src: '../assets/preview/preview.png'})

template.use_premade("description", {
  name: template.metadata.name,
  long_description:
    "is a powerful temporary email generator that allows you to scrape thousands of emails Python! Email Scraper uses [fyii.de trashmail provider](https://fyii.de/trashmail/) to generate emails. All emails are unique and have their own inboxes in which emails can be received from. Use email-scraper to use services where you don't want to provide your own email address.",
});

template.use_component("./readme_components/install.md");
template.use_premade("license", {
  author: template.metadata.author.name,
  email: template.metadata.author.email,
  license: template.metadata.license,
});

template.make_readme();
