class CardNews extends HTMLElement {
    constructor() {
        super();
        const shadow = this.attachShadow({ mode: "open" })
        shadow.appendChild(this.build());
        shadow.appendChild(this.style());
    }

    build() {
        const componentRoot = document.createElement("div");
        componentRoot.setAttribute("class", "card");

        const cardLeft = document.createElement("div");
        cardLeft.setAttribute("class", "card-left");

        const author = document.createElement("span");
        author.textContent = "Vagas de Emprego"

        const bbreak = document.createElement("br");

        const authorInfo = document.createElement("span");
        const authorImg = document.createElement("img");
        authorImg.src = "../../assets/mutley.jpg"
        authorImg.alt = "Foto do Mutley";
        authorInfo.appendChild(authorImg);
        authorInfo.appendChild(document.createTextNode("Mutley Vigarista"))

        const linkTitle = document.createElement("h1");
        linkTitle.textContent = "Dick Vigarista Contrata Devs";

        const newsContent = document.createElement("p");
        newsContent.textContent = `Procura-se Devs que saibam trabalhar sobre pressão, para trabalhar no Project Catch the Pigeon. Ambiente acolhedor e amigável, dando enfase no crescimento pessoal. Café por conta da casa.`

        cardLeft.appendChild(author);
        cardLeft.appendChild(document.createElement("br"));
        cardLeft.appendChild(authorInfo);
        cardLeft.appendChild(linkTitle);
        cardLeft.appendChild(newsContent);

        const cardRight = document.createElement("div");
        cardRight.setAttribute("class", "card-right");

        const newsImage = document.createElement("img");
        newsImage.src = "../../assets/dick.jpg"
        newsImage.alt = "Imagem da notícia";

        cardRight.appendChild(newsImage);

        componentRoot.appendChild(cardLeft);
        componentRoot.appendChild(cardRight);

        return componentRoot;
    }

    style() {
        const style = document.createElement("style");
        style.textContent = `.card{
        .card {
  background-color: white;
  width: 750px;
  border: 1px solid red;
  display: flex;
  flex-direction: row;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
}

.card-left {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  padding: 25px 30px;
  border-right: 1px solid blue;
}

.card-left span {
  color: rgb(152, 151, 151);
  font-size: 14px;
  margin-bottom: 6px;
  display: flex;
  align-items: center;
  gap: 6px;
}

.card-left span img {
  width: 20px;
  height: 20px;
  border-radius: 50%;
  border: 1px solid red;
}

.card-left h1 {
  font-size: 26px;
  margin: 15px 0;
  color: #222;
}

.card-left p {
  color: gray;
  line-height: 1.5;
}

.card-right {
  width: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  padding: 20px;
}

.card-right img {
  max-width: 100%;
  border-radius: 5px;
}

.btn-requisitos {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  border: 1px solid blue;
}

.btn-requisitos button {
  padding: 10px 20px;
  font-size: 16px;
  background-color: black;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn-requisitos button:hover {
  background-color: darkred;
}

@media (max-width: 800px) {
  .card {
    flex-direction: column;
    width: 100%;
    max-width: 400px;
  }
  .card-left {
    border-right: none;
    border-bottom: 1px solid blue;
    padding: 20px;
  }
  .btn-requisitos {
    border-left: none;
    padding: 15px;
  }
  .card-right {
    width: 100%;
    padding: 15px;
  }
}       
        }`;

        return style
    }

}

customElements.define('card-news', CardNews)