import QtQuick 2.5
import QtQuick.Controls 1.4
import QtQuick.Controls.Styles 1.4

import "../../qmlStyles"

Rectangle {
    id: root
    anchors.fill: parent
    anchors.margins: 20
    state: "answeringInProgress"

    property ListModel testModel: ListModel {}
    property int correctAnswers: 0
    property int totalAnswers: 0
    property int questionsCount: 0

    function init(){
        correctAnswers = totalAnswers = questionsCount = 0
    }

    function setTestModel(tests){
        testModel.clear()
        testModel.append(tests)
    }

    function questionAnswered(id){
        var answered = false
        for(var i = 0; i < testModel.count; ++i) {
            if (testModel.get(i).id == id && testModel.get(i).answered == true)
                answered = true
        }
        return answered
    }

    ScrollView {
        id: testsScroll
        anchors.fill: parent

        ListView {
            id: testsView
            anchors.fill: parent
            model: testModel

            delegate: answersDelegate

            section.property: "question"
            section.delegate: questionDelegate

        }
        style: ScrollBarStyle {}
    }

    Component {
        id: questionDelegate

        Rectangle{
            id: questionRect
            width: parent.width
            height: 40
            color: "#ffd200"

            Text {
                anchors.left: parent.left
                anchors.leftMargin: 10
                anchors.verticalCenter: parent.verticalCenter
                color: "#000000"
                font.family: "Helvetica"
                font.pixelSize: 24
                text: section
                wrapMode: Text.Wrap
            }

            Component.onCompleted: {
                questionsCount += 1
            }
        }
    }

    Component {
        id: answersDelegate
        Item {
            id: oneItem
            width: parent.width
            height: 30

            Rectangle {
                id: answerRectangle

                anchors.fill: parent
                anchors.leftMargin: 15
                anchors.rightMargin: 15
                anchors.topMargin: -1
                anchors.bottomMargin: 1

                Text {
                    anchors.left: parent.left
                    anchors.leftMargin: 30
                    anchors.verticalCenter: parent.verticalCenter
                    color: "#000000"
                    font.family: "Helvetica"
                    font.pixelSize: 24
                    text: content
                    wrapMode: Text.Wrap
                }

                Rectangle {
                    id: lineRect
                    anchors.left: parent.left
                    anchors.right: parent.right
                    height: 1
                    color: "#000000"
                }

                MouseArea {
                    anchors.fill: parent
                    onClicked: {
                        if (!(answered || questionAnswered(id))){
                                answered = true
                                answerRectangle.color = (correct == true) ? "#00ff00": "#ff0000"
                                totalAnswers += 1
                                if (correct) correctAnswers += 1
                        }
                        else return;
                        if(totalAnswers == questionsCount){
                            var component = Qt.createComponent("ResultDialog.qml");
                            if (component.status === Component.Ready) {
                                var dialog = component.createObject(parent,{popupType: 1});
                                dialogConnection.target = dialog
                                dialog.show();
                            }
                        }
                    }
                }
            }
        }
    }
    Connections {
        id: dialogConnection
        onVisibleChanged: {
            target.answeredCount = correctAnswers
            target.totalCount = totalAnswers
        }
    }
}
