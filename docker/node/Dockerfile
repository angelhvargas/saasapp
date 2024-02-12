# Use a slimmer Node.js base image
FROM node:20-slim

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json for npm install
COPY package*.json ./

# Install dependencies (including 'build-essential' for native dependencies)
RUN apt-get update && apt-get install -y python3 build-essential && rm -rf /var/lib/apt/lists/* \
    && npm install

# Copy the rest of your application code
COPY . .

# Expose port 8080 if your application needs it
EXPOSE 8080

# Command to run your app (adjust as necessary)
CMD ["npm", "start"]
