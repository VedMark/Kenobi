import QtQuick 2.5

Item {
    id: root
    width: parent.width
    height: 50

    property alias text: textitem.text
    signal clicked

    Text {
        id: textitem
        color: "#000000"
        font.pixelSize: 32
        text: modelData
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
        anchors.leftMargin: 50
    }

    Rectangle {
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.margins: 15
        height: 1
        color: "#000000"
    }

    MouseArea {
        id: mouse
        anchors.fill: parent
        onClicked: root.clicked()
    }
}
