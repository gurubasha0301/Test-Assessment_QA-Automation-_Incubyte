Feature: User Registration
  As a new user
  I want to sign up on the Magento website
  So that I can access my account dashboard

  Scenario: Successful registration with valid details
    Given I am on the Magento home page
    When I navigate to the "Create an Account" page
    And I fill in the registration form with valid details
      | Field      | Value                |
      | First Name | Safiya                 |
      | Last Name  | Guru                  |
      | Email      | dh6deyadfd1@gmail.com |
      | Password   | hKhdr1dfd57@         |
    And I submit the form
    Then I should be redirected to the account dashboard
