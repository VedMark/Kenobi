import QtQuick 2.5
import QtQuick.Window 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

ScrollViewStyle {
    transientScrollBars: true
    decrementControl: Item {}
    incrementControl: Item {}
    handle: Item {
        implicitWidth: 14
        implicitHeight: 26
        Rectangle {
            color: "#000000"
            radius: 3
            anchors.fill: parent
            anchors.topMargin: 4
            anchors.leftMargin: 4
            anchors.rightMargin: 4
            anchors.bottomMargin: 4
        }
    }
    scrollBarBackground: Item {
        implicitWidth: 14
        implicitHeight: 26
    }
}