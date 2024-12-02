#include <WiFi.h>
#include <WebServer.h>
#include <SPIFFS.h>

int led = 2;
WebServer server(80);
bool etat = 0;

void handleRoot(){
  String page = "<!DOCTYPE html>";
  page += "<html lang='pt-br'>";
  page += "<head>";
  page += "<meta charset='UTF-8'>";
  page += "<meta name='viewport' content='width=device-width, initial-scale=1.0'>";
  page += "<title>WiFi Controller</title>";
  page += "<link rel='stylesheet' href='/style.css'>";
  page += "<script src='script.js'></script>";
  page += "</head>";
  page += "<body>";

  page += "<header>";
  page += "<h1>ESP32 controller</h1>";
  page += "</header>";
      
  page += "<div class='buttons'>";
  page += "<button id = 'btn-on' onclick='on()'>On</button>";
  page += "<button id = 'btn-off' onclick='off()'>Off</button>";
  page += "</div>";
  page += "</body>";
  page += "</html>";

  server.send(200, "text/html", page);
  server.serveStatic("style.css", SPIFFS, "style.css");
}

void handleNotFound(){
  server.send(404, "text/plan", "404: Nao encontrado!");
}

void on(){
  etat = 1;
  digitalWrite(led,HIGH);
  server.sendHeader("Location", "/");
  server.send(303);
}

void off(){
  etat = 0;
  digitalWrite(led,LOW);
  server.sendHeader("Location", "/");
  server.send(303);
}

void setup() {
    pinMode(led,OUTPUT);
    digitalWrite(led,LOW);


    Serial.begin(115200);
    delay(1000);
    Serial.println("\n");

    WiFi.begin("Linux", "kingson1976");
    Serial.print("En connectant...");

    while(WiFi.status() != WL_CONNECTED){
      Serial.print(".");
      delay(100);
    }

    Serial.println("\n");
    Serial.print("Connexion etablie!");
    Serial.println("Adresse IP: ");
    Serial.println(WiFi.localIP());

    server.on("/", handleRoot);
    server.onNotFound(handleNotFound);
    server.begin();
    Serial.println("Servidor Ativado");
}

void loop() {
  server.handleClient();
} 