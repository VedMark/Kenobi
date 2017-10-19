import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

Rectangle {
    property int heightRect: 704

    id: schedulePanel
    border.width: 3
    height: heightRect
    state: "collapsed"

    Text {
        id: title
        anchors.centerIn: parent
        font.pixelSize: 16
        font.bold: true
        font.family: "Helvetica"
        color: "#000000"
        text: "Schedule"
        transform: Rotation {origin.y: -25; axis { x: 0; y: 0; z: 1 } angle: 270 }
    }

    states: [
        State {
            name: "collapsed"
            PropertyChanges {
                target: schedulePanel
                color: "#ffd200"
                width: 25
                height: heightRect
            }
            PropertyChanges {
                target: groupsList
                visible: false
            }
            PropertyChanges {
                target: scheduleList
                visible: false
            }
            PropertyChanges {
                target: title
                visible: true
            }
        },

        State {
            name: "deployed"
            PropertyChanges {
                target: schedulePanel
                color: "#FFFFFF"
                width: 300
                height: heightRect
            }
            PropertyChanges {
                target: groupsList
                visible: true
            }
            PropertyChanges {
                target: scheduleList
                visible: true
            }
            PropertyChanges {
                target: title
                visible: false
            }
        }
    ]

    MouseArea {
        anchors.fill: parent

        onClicked: {
            if (parent.state == "deployed")
                parent.state = "collapsed"
            else
                parent.state = "deployed"
            scheduleView.getGroups()
            scheduleView.getSchedules(groupsList.currentText)
        }
    }

    function setScheduleModel(newElement) {
        scheduleList.model.clear()
        scheduleList.model.append(newElement)
    }

    ListModel {
        id: scheduleModel
    }

    ListView {
        id: scheduleList
        anchors.fill: parent
        anchors.margins: 50
        anchors.topMargin: 75
        clip: true
        model: scheduleModel
        delegate: scheduleItem

        section.property: "day"
        section.delegate: sectionDelegate
    }

    Component {
        id: scheduleItem
        Rectangle {
            anchors.left: parent.left
            anchors.leftMargin: 15
            width: parent.width
            height: 20

            Row {
                spacing: 15
                Text {
                    font.pixelSize: 14
                    font.family: "Helvetica"
                    text: lesson
                    color: "#000000"
                }
                Text {
                    font.pixelSize: 14
                    font.family: "Helvetica"
                    text: subject
                    color: "#000000"
                }
            }
        }
    }

    Component {
        id: sectionDelegate

        Rectangle {
            width: ListView.view.width
            height: 25
            color: "#ffd500"
            border.width: 3
            border.color: "#000000"
            Text {
                id: label
                anchors.centerIn: parent
                font.pixelSize: 16
                font.bold: true
                font.family: "Helvetica"
                color: "#000000"
                text: section
            }
        }
    }

    ComboBox {
        id: groupsList
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.left: parent.left
        anchors.leftMargin: 50
        anchors.top: parent.top
        anchors.topMargin: 25
        currentIndex: 0
        height: 25
        model: groupsModel

        style: ComboBoxStyle {
            background: Rectangle {
              id: rectCategory
              color: "#38300a"
            }

            label: Item {
                anchors.fill: parent
                Text {
                    anchors.horizontalCenter: parent.horizontalCenter
                    anchors.verticalCenter: parent.verticalCenter
                    font.pointSize: 14
                    font.family: "Helvetica"
                    color: "#FFFFFF"
                    text: control.currentText + " grade"
                }
            }

            property Component __dropDownStyle: MenuStyle {
                __maxPopupHeight: 600
                __menuItemType: "comboboxitem"

                frame: Rectangle {
                    color: "#FFFFFF"
                    border.width: 0
                }

                itemDelegate.label:
                    Text {
                    verticalAlignment: Text.AlignVCenter
                    horizontalAlignment: Text.AlignHCenter
                    font.pointSize: 14
                    font.family: "Helvetica"
                    font.capitalization: Font.SmallCaps
                    color: styleData.selected ? "#FFFFFF" : "#000000"
                    text: styleData.text
                }

                itemDelegate.background: Rectangle {
                    color: styleData.selected ? "#ffe772" : "#FFFFFF"
                }

            }
        }

        onCurrentIndexChanged: {
            scheduleView.getSchedules(groupsList.currentText)
        }
    }
}
