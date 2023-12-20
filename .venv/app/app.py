from shiny import App, render, ui

app_ui = ui.page_fluid(
    ui.panel_title("Annuaire Electronique des Entreprises Ivoiriennes"),
    ui.layout_sidebar(
        ui.panel_sidebar(
            ui.input_text("NomEntreprise", 
                          "Entrez le Nom d'une entreprise", 
                          placeholder="Entreprise"
                          ),
            ui.input_text("SecteurActivite", 
                          "Entrez le secteur d'activite", 
                          placeholder="Secteur"
                          ),
            ui.input_selectize("SecteurActivite", 
                               "Choisir un secteur d'activite",
                               choices=("EntsA", "EntsB", "EntsC")
                               ),
            ui.input_selectize("Lieu", 
                               "Choisir un lieu",
                               choices=("LieuA", "LieuB", "LieuC")
                               )


        )
    )
)


def server(input, output, session):
    @render.text
    def txt():
        return f"n*2 is {input.n() * 2}"


app = App(app_ui, server)
