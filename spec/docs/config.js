async function loadTurtle() {
  //this is the function you call in 'preProcess', to load the highlighter
  const worker = await new Promise(resolve => {
    require(["core/worker"], ({ worker }) => resolve(worker));
  });
  const action = "highlight-load-lang";
  const langURL =
    "https://cdn.jsdelivr.net/gh/redmer/highlightjs-turtle/src/languages/turtle.js";
  const propName = "hljsDefineTurtle"; // This funtion is defined in the highlighter being loaded
  const lang = "turtle"; // this is the class you use to identify the language
  worker.postMessage({ action, langURL, propName, lang });
  return new Promise(resolve => {
    worker.addEventListener("message", function listener({ data }) {
      const { action: responseAction, lang: responseLang } = data;
      if (responseAction === action && responseLang === lang) {
        worker.removeEventListener("message", listener);
        resolve();
      }
    });
  });
}

var respecConfig = {
  // check https://respec.org/docs/ for the meaning of these keys
  preProcess: [loadTurtle],
  authors: [
    {
      name: "Pano Maria",
      company: "Skemu",
      url: "https://skemu.com",
      orcid: "0009-0000-2598-1894",
      companyURL: "https://skemu.com"
    },
    {
      name: "Anastasia Dimou",
      mailto: "anastasia.dimou@kuleuven.be",
      company: "KU Leuven",
      orcid: "0000-0003-2138-7972",
      companyURL: "https://dtai.cs.kuleuven.be/"
    },
  ],
  edDraftURI: "https://w3id.org/rml/core/spec",
  editors: [
    {
      name: "Pano Maria",
      company: "Skemu",
      url: "https://skemu.com",
      orcid: "0009-0000-2598-1894",
      companyURL: "https://skemu.com"
    },
    {
      name: "Anastasia Dimou",
      mailto: "anastasia.dimou@kuleuven.be",
      company: "KU Leuven",
      orcid: "0000-0003-2138-7972",
      companyURL: "https://dtai.cs.kuleuven.be/"
    },
  ],
  formerEditors: [
  ],
  github: "https://github.com/kg-construct/rml-core",
  license: "w3c-software-doc",
  localBiblio: {
    RML: {
        title: "RDF Mapping Language (RML)",
        href: "https://rml.io/specs/rml/",
        status: "Unofficial Draft",
        publisher: "",
        date: "",
      },
  },
  otherLinks: [
    {
      key: "Website",
      data: [{
        value: "https://rml.io",
        href: "https://rml.io"
      },
      {
        value: "https://fno.io",
        href: "https://fno.io"
      }]
    },
  ],
  shortName: "RML-Core",
  specStatus: "CG-DRAFT",
  // W3C config
  copyrightStart: "2021",
  doJsonLd: true,
  group: "kg-construct",
};
