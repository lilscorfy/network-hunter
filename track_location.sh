#!/bin/bash

echo "📍 Fetching device location..."
location=$(termux-location 2>/dev/null)  # Capture errors silently

# Check if the command ran successfully
if [ -z "$location" ]; then
    echo "❌ Error: Unable to fetch location. Make sure Termux has location permission!"
    exit 1
fi

# Extract latitude and longitude using jq (check if values exist)
latitude=$(echo "$location" | jq -r '.latitude // empty')
longitude=$(echo "$location" | jq -r '.longitude // empty')

if [[ -z "$latitude" || -z "$longitude" ]]; then
    echo "❌ Failed to get location. Ensure GPS is ON and permissions are granted!"
    echo "Raw output from termux-location: $location"
    exit 1
fi

# Display and log the location
echo "✅ Location Found!"
echo "Latitude: $latitude"
echo "Longitude: $longitude"
echo "Timestamp: $(date)"

# Save to log file
echo "$(date) - Lat: $latitude, Lon: $longitude" >> location_log.txt#!/bin/bash

echo "📍 Fetching device location..."
location=$(termux-location 2>/dev/null)  # Capture errors silently

# Check if the command ran successfully
if [ -z "$location" ]; then
    echo "❌ Error: Unable to fetch location. Make sure Termux has location permission!"
    exit 1
fi

# Extract latitude and longitude using jq
latitude=$(echo "$location" | jq -r '.latitude // empty')
longitude=$(echo "$location" | jq -r '.longitude // empty')

# Verify that values are valid
if [ -n "$latitude" ] && [ -n "$longitude" ]; then
    echo "✅ Location Found!"
    echo "Latitude: $latitude"
    echo "Longitude: $longitude"
    echo "Timestamp: $(date)"

    # Save location to log file
    echo "$(date) - Lat: $latitude, Lon: $longitude" >> location_log.txt
else
    echo "❌ Failed to get location. Ensure GPS is ON and permissions are granted!"
fi
