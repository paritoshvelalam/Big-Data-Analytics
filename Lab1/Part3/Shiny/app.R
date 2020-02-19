#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#





library(shiny)
library(shinyWidgets)
# Define UI for application that draws a histogram
ui <- fluidPage(
  
  
   
   # Application title
   titlePanel("CDC vs Twitter"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
        
        actionButton("button1", "CDC Map"),
        actionButton("button2", "Twitter Map"),
        selectInput("twittermap","CDC Map vs Twitter",c(None="none",AllSearchwords="tw1",FluKeyword="tw2",FeverKeyword="tw3")),
      h4("Analysis:",position="left"),
      textOutput("inttext")
        
        ),
      
      # Show a plot of the generated distribution
      mainPanel( 
                uiOutput("img1"),
                #img(src='CDC.png',align="middle", height = 600, width = 600),
                uiOutput("img2",align="left"), 
                position="right")
      
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   
   output$img2 <- renderUI({
     
     
    if(input$twittermap=="tw1"){
      img(src='allsearchwords.png', align = "middle", height = 600, width = 600)
    }
     else if(input$twittermap=="tw2"){
       img(src='flu.png', align = "middle", height = 600, width = 600)
     }
     else if(input$twittermap=="tw3"){
       img(src='fever.png', align = "middle", height = 600, width = 600)
     }
   })

   
   output$inttext <- renderText({
     if(input$twittermap=="tw1"){
       print("Upon looking both the maps, it is observed for some states the heat map generated using Twitter shows high flu level while the CDC Heat Map shows low level.")
     }
     else if(input$twittermap=="tw2"){
       print("Analysing both the maps, the results for Texas State match (Twitter as well as CDC)")
     }
     else if(input$twittermap=="tw3"){
       print("Heat map for California State generated using Twitter data contradicts CDC Heat map.")
     }
   })
   
   observeEvent(input$button1,{
     
     output$img1 <- renderUI({
     img(src='CDC.png', align = "middle", height = 600, width = 600)})
     
     
   })
   
   
   observeEvent(input$button2,{
     
     output$img1 <- renderUI({
       img(src='allsearchwords.png', align = "middle", height = 600, width = 600)})
     
     
   })
     
   }
   
   
   
   
   
   
   
   
   
   

# Run the application 
shinyApp(ui = ui, server = server)

