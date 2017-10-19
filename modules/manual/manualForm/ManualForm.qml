import QtQuick 2.5
import QtQuick.Window 2.0
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

Rectangle {
    id: contentWidget
    width: 1335
    height: 704
    border.width: 3
    
    property string titlePr: stackView.depth > 1 ? stackView.currentItem.model.title : "Tutorial"

    Rectangle {
        id: titleWdt
        width: parent.width
        height: contentWidget.height*0.1
        color: "#ffd200"
        border.width: 3

        Rectangle {
            id: backButton
            anchors.left: parent.left
            width: opacity ? 60 : 0
            height: parent.height
            opacity: stackView.depth > 1 ? 1 : 0
            border.width: 3
            color: backmouse.pressed ? "#ffd200" : "#ffb500"
            Image {
                anchors.centerIn: parent
                anchors.fill: parent
                fillMode: Image.PreserveAspectFit
                source: "images/previous_page.png"
            }
            MouseArea {
                id: backmouse
                anchors.fill: parent
                onClicked: {
                    stackView.pop()
                    titlePr = stackView.depth > 1
                        ? titlePr.substr(0, titlePr.lastIndexOf(": "))
                        : "Tutorial"
                }
            }
        }

        Text {
            id: titleTxt
            Behavior on x { NumberAnimation{ easing.type: Easing.OutCubic} }
            anchors.left: parent.left
            anchors.leftMargin: backButton.x + backButton.width + 10
            anchors.right: parent.right
            anchors.verticalCenter: parent.verticalCenter
            font.bold: true
            font.family: "Helvetica"
            font.pixelSize: contentWidget.height * 0.05
            color: "#000000"
            text: titlePr
            wrapMode: Text.Wrap
        }
    }

    function setSectionsModel(newModel) {
        sectionsModel.clear()
        sectionsModel.append(newModel)
    }

    function setTopicsModel(newModel) {
        topicsModel.clear()
        topicsModel.append(newModel)
    }

    StackView {
        id: stackView
        anchors.fill: parent
        anchors.topMargin: titleWdt.height

        initialItem: sectionsComponent

        ListModel {
            id: sectionsModel
        }

        Component {
            id: sectionsComponent
            ScrollView {
                id: sectionsScroll
                anchors.top: parent.top
                anchors.topMargin: 10
                width: parent.width
                height: parent.height

                ListView {
                    id: sectionsView
                    anchors.left: parent.left
                    anchors.top: parent.top
                    width: parent.width
                    height:parent.height
                    model: sectionsModel
                    delegate: ManualDelegate {
                        text: title
                        onClicked: {
                            titlePr = model.title
                            var sectId = model.sectionId
                            stackView.push(topicsComponent)
                            manualView.getTopics(sectId)
                        }
                    }
                }
                style: ScrollBarStyle {}
            }
        }

        ListModel {
            id: topicsModel
        }

        Component {
            id: topicsComponent
            ScrollView {
                id: topicsScroll
                anchors.top: parent.top
                anchors.topMargin: 10
                width: parent.width
                height: parent.height

                ListView {
                    id: topicsView
                    anchors.left: parent.left
                    anchors.top: parent.top
                    width: parent.width
                    height: parent.height
                    model: topicsModel
                    delegate: ManualDelegate {
                        text: title
                        onClicked: {
                            titlePr = titlePr + ": " + model.title
                            stackView.push({item: contentComponent, properties: {content: model.content}})
                        }
                    }
                }
                style: ScrollBarStyle {}
            }
        }

        Component {
            id: contentComponent

            TextArea {
                id: contentTxt

                property alias content: contentTxt.text

                width: parent.width
                height: parent.height
                font.family: "Helvetica"
                font.pixelSize: 14
                menu: Item {}
                readOnly: true
                textFormat: Text.RichText
                textMargin: 10
                wrapMode: Text.Wrap

                style: TextAreaStyle {
                    transientScrollBars: true
                    decrementControl: Item {}
                    incrementControl: Item {}
                    frame: Item {}

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
            }
        }
    }
}
