import React from 'react';
import axios from 'axios';
import {Table} from 'antd';
class Connections extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            connections: [],
            loading: true
        }
    }

    async getConnectionsData() {
        try {
            const res = await axios.get('http://localhost:8080/api/v1/connection')
            this.setState({ loading: false, connections: res.data })
        } catch {
            console.error("Could not get connections")
        }
    }

    componentDidMount() {
        this.getConnectionsData()
    }

    render() {
        const columns = [
            {
                title: 'ID',
                key: 'id',
                dataIndex: 'id'
            },
            {
                title: 'Name',
                key: 'name',
                dataIndex: 'name'
            },
            {
                title: 'Type',
                key: 'type',
                dataIndex: 'type'
            },
            {
                title: 'Schema',
                key: 'schema_blob',
                dataIndex: 'schema_blob',
                render: d => JSON.stringify(d)
            }
        ]
        return (<div style={{ height: 400, width: '70%' }}>
                <Table
                    dataSource = {this.state.connections}
                    columns = {columns}
                />
                </div>
        );
    }
}

export default Connections;