import XCTest

final class SmokeTests: XCTestCase {
    func testCoreJourneyAndPersistence() {
        continueAfterFailure = false
        let app = XCUIApplication()
        app.launchArguments = ["--uitest-reset"]
        app.launch()
        XCTAssertTrue(app.buttons["continueLesson"].waitForExistence(timeout: 15))
        capture("01-today")
        app.buttons["continueLesson"].tap()
        XCTAssertTrue(app.staticTexts["lessonTitle"].waitForExistence(timeout: 5))
        capture("02-lesson")
        app.buttons["saveLesson"].tap()
        XCTAssertEqual(app.buttons["saveLesson"].label, "Unsave lesson")
        app.terminate()
        app.launchArguments = []
        app.launch()
        app.buttons["continueLesson"].tap()
        XCTAssertEqual(app.buttons["saveLesson"].label, "Unsave lesson")
        app.tabBars.buttons["Learn"].tap()
        XCTAssertTrue(app.textFields["librarySearch"].waitForExistence(timeout: 5))
        capture("03-learning-path")
        app.textFields["librarySearch"].tap()
        app.textFields["librarySearch"].typeText("delay throw")
        XCTAssertTrue(app.staticTexts["Throw the last word into space"].waitForExistence(timeout: 5))
        app.buttons["dismissSearch"].tap()
        XCTAssertTrue(app.tabBars.buttons["Sessions"].isHittable)
        app.tabBars.buttons["Sessions"].tap()
        app.buttons["workflow-record-session"].tap()
        XCTAssertTrue(app.buttons["workflowStep0"].waitForExistence(timeout: 5))
        app.buttons["workflowStep0"].tap()
        XCTAssertTrue(app.buttons["workflowStep0"].label.contains("Step 1, complete:"))
        capture("04-session")
        app.tabBars.buttons["Ask"].tap()
        app.buttons["suggestion-How do I throw a delay?"].tap()
        XCTAssertTrue(app.staticTexts["assistantAnswer"].waitForExistence(timeout: 5))
        XCTAssertTrue(app.staticTexts["assistantAnswer"].label.contains("send"))
        app.swipeUp()
        capture("05-assistant")
        app.tabBars.buttons["Studio"].tap()
        capture("06-studio")
        app.buttons["delayLab"].tap()
        XCTAssertTrue(app.staticTexts["bpmValue"].waitForExistence(timeout: 5))
        XCTAssertEqual(app.staticTexts["bpmValue"].label, "90")
        capture("07-delay-lab")
    }
    private func capture(_ name: String) {
        let attachment = XCTAttachment(screenshot: XCUIScreen.main.screenshot())
        attachment.name = name
        attachment.lifetime = .keepAlways
        add(attachment)
    }
}
