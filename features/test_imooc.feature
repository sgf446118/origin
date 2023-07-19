Feature: test_imooc

@mytest1
  Scenario:login imooc
    Given open chrome browser
    And input url <https://www.imooc.com>
    When click login button
    And input user id
    And input password
    And click to login
    Then verify login success
    And close browser