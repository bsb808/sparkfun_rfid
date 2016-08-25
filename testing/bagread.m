
 % Load the data file
bag = rosbag('rfid.bag');
bag.AvailableTopics    % Prints the list of topics
 
 
% Extract pose data 
bagId = select(bag,'Topic','/rfid');
msg = readMessages(bagId);
msg{1}.showdetails
tsId = timeseries(bagId)
