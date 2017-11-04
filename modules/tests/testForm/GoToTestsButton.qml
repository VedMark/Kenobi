import QtQuick 2.6
import QtQuick.Controls 1.4

Rectangle {
    id: root
    width: testTxt.width + 30
    border.width: 3
    color: testMouseArea.pressed ? "#000000" : "#38300a"

    signal clicked()

    Text {
        id: testTxt
        anchors.centerIn: parent
        text: "Test"
        color: "#FFFFFF"
        font.family: "Helvetica"
        font.pixelSize: 20
    }

    MouseArea {
        id: testMouseArea
        anchors.fill: parent
        onClicked: root.clicked()
    }
}
