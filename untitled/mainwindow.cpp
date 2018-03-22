#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QDebug>
#include <QTcpSocket>
MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    Qser = new QTcpServer(this);
    Qser->listen(QHostAddress("127.0.0.1"),8080);
    connect(Qser, SIGNAL(newConnection()), this, SLOT(newClient()));

}
void MainWindow::NewCon()
{
    qDebug()<< "have cline\r\n";

}
void MainWindow::newClient()
{
       QTcpSocket *tcpClient = Qser->nextPendingConnection();
       qDebug() << "Client connected: ";
       connect(tcpClient, SIGNAL(disconnected()), tcpClient, SLOT(deleteLater()));
       connect(tcpClient, SIGNAL(readyRead()), this, SLOT(readData()));
}

void MainWindow::deleteLater()
{
    qDebug() << "Client disconnect: ";

}
void MainWindow::readData()
{
    QTcpSocket* myClient = qobject_cast<QTcpSocket*>(sender());
    QByteArray data = myClient->readAll();
    qDebug()<< data;
   // sendData(myClient, data);
}

MainWindow::~MainWindow()
{
    delete ui;
}
