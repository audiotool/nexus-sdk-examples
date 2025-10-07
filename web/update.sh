# cd ../nexus && npm run build && cp audiotool-nexus-0.0.1.tgz ../nexus-examples/.
# cd ../nexus-examples
for dir in examples/*/; do
    if [ -d "$dir" ]; then
        cd "$dir"
        echo "updating $dir"
        npm i ../../audiotool-nexus-0.0.1.tgz
        cd ../../
    fi
done
