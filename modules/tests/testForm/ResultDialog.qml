import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Layouts 1.1
import QtQuick.Window 2.0

Window {
    id: mypopDialog
    title: "MyPopup"
    width: 300
    height: 120
    flags: Qt.Dialog
    modality: Qt.WindowModal
    property variant answeredCount: -1
    property variant totalCount: -1

    ColumnLayout {
        anchors.fill: parent
        anchors.margins: 10

        Rectangle{
            anchors.left: parent.left
            Layout.preferredWidth: parent.width
            Layout.preferredHeight: 40

            Text{
                anchors.centerIn: parent
                color: "#000000"
                font.family: "Helvetica"
                font.pixelSize: 24
                text: "Your score: " + answeredCount + "/" + totalCount
            }
        }

        Rectangle {
            Layout.preferredWidth: parent.width
            Layout.preferredHeight: 30
            Button {
                text: "Ok"
                anchors.centerIn: parent
                onClicked: {
                    mypopDialog.close();
                }
            }
        }
    }
}