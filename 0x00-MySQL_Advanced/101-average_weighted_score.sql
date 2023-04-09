CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE user_cursor CURSOR FOR SELECT DISTINCT user_id FROM grades;
    DECLARE current_user_id INT;
    DECLARE total_score DECIMAL(10,2);
    DECLARE total_weight DECIMAL(10,2);
    DECLARE average_score DECIMAL(10,2);

    OPEN user_cursor;
    FETCH NEXT FROM user_cursor INTO current_user_id;

    WHILE @@FETCH_STATUS = 0 DO
        SELECT SUM(score) INTO total_score FROM grades WHERE user_id = current_user_id;
        SELECT SUM(CASE
                    WHEN subject = 'Math' THEN 4.0
                    WHEN subject = 'Science' THEN 3.5
                    WHEN subject = 'English' THEN 3.0
                    ELSE 2.5
                 END) INTO total_weight FROM grades WHERE user_id = current_user_id;

        SET average_score = total_score / total_weight;

        INSERT INTO average_scores (user_id, score) VALUES (current_user_id, average_score);

        FETCH NEXT FROM user_cursor INTO current_user_id;
    END WHILE;

    CLOSE user_cursor;
END;
