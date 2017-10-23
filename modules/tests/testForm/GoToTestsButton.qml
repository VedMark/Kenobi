import QtQuick 2.6
import QtQuick.Controls 1.4

Rectangle {
    id: root
    width: testTxt.width + 30
    border.width: 3
    color: testMouseArea.pressed ? "#ff8421" : "#d87e36"

    signal clicked()

    Text {
        id: testTxt
        anchors.centerIn: parent
        text: "Test"
        font.family: "Helvetica"
        font.pixelSize: 20
    }

    MouseArea {
        id: testMouseArea
        anchors.fill: parent
        onClicked: root.clicked()
    }
}
